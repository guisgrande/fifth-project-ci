from django.shortcuts import redirect, reverse, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from products.models import Product
from products.forms import ProductForm
from checkout.models import Order
from .models import NewsLetterList, NewsLetterMail
from .forms import StockForm, OrderStatusForm


@login_required
def add_product(request):
    """
    A view to admin add new products to store database
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_details', args=[product.slug]))
        else:
            messages.error(request, 'Failed to add product. Review form.')
    else:
        form = ProductForm()

    template = 'management/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, slug):
    """
    A view to admin edit products from store database
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {product.name}!')
            return redirect(reverse('product_details', args=[product.slug]))
        else:
            messages.error(request, 'Failed to update product. Review form.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'management/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, slug):
    """
    A view to admin delete products from store database
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted!')
        return redirect(reverse('products'))

    template = 'management/delete_product.html'
    context = {
        'product': product,
    }

    return render(request, template, context)


def news_letter_sub(request):
    """
    A view to user subscribe to news letter list
    """
    if request.method == 'POST':
        name = request.POST.get('news_name', None)
        email = request.POST.get('news_email', None)

        if not name or not email:
            messages.error(request,
                           "You must use legit name and email to subscribe")
            return redirect("/")

        if get_user_model().objects.filter(email=email).first():
            if request.user.is_authenticated:
                if email == request.user.email:
                    pass
            else:
                messages.error(request, f'''Found registered user with associated
                               {email} email. Login first''')
                return redirect(request.META.get("HTTP_REFERER", "/"))

        subscribe_user = NewsLetterList.objects.filter(
                                                news_email=email).first()

        if subscribe_user:
            messages.error(request,
                           f"{email} email address is already subscribed.")
            return redirect(request.META.get("HTTP_REFERER", "/"))

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        subscribe_model_instance = NewsLetterList()
        subscribe_model_instance.news_name = name
        subscribe_model_instance.news_email = email
        subscribe_model_instance.save()

        subject = str('Street Craft - News Letter Subscrition')
        body = render_to_string(
            'management/confirmation_emails/confirmation_news_letter_sub.txt',
            {'name': name, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [email]
        )

        messages.success(request,
                         f'{email} was successfully subscribed to News Letter')
        return redirect(request.META.get("HTTP_REFERER", "/"))


@login_required
def news_letter_view(request):
    """
    A view to display News Letter email form.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can view this page.')
        return redirect(reverse('home'))

    return render(request, 'management/admin_news_letter.html')


@login_required
def news_letter_send(request):
    """
    A view to site owner send News Letter email to subscribers
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, just site owner can send emails.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        subject = request.POST.get('subject', None)
        body = request.POST.get('body', None)

        if not subject or not body:
            messages.error(request, "You forgot to fill in one of the fields.")
            return redirect("/")

        email_list = []
        for subscriber in NewsLetterList.objects.all():
            email_list.append(subscriber.news_email)

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [email_list]
        )

        news_letter_mails = NewsLetterMail()
        news_letter_mails.subject = subject
        news_letter_mails.body = body
        news_letter_mails.status = 1
        news_letter_mails.save()

        messages.success(request,
                         'News Letter successfully sent to mailing list!')
        return redirect(request.META.get("HTTP_REFERER", "/"))


@login_required
def stock_control(request):
    """
    A view to display Stock control template.
    """

    product_list = Product.objects.all()
    form = StockForm()

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can view this page.')
        return redirect(reverse('home'))

    context = {
        'product_list': product_list,
        'form': form,
    }

    return render(request, 'management/admin_stock.html', context)


@login_required
def update_stock(request, slug):
    """
    A view to admin / site owner update stock quantity
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can view this page.')
        return redirect(reverse('home'))

    product = Product.objects.get(slug=slug)

    if request.method == 'POST':
        form = StockForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request,
                             f'Successfully updated {product.name} quantity')
            return redirect(reverse('stock_control'))
        else:
            messages.error(request, 'Failed to update stock.')
    else:
        form = StockForm(instance=slug)

    template = 'management/admin_stock.html'
    context = {
        'product': product,
    }

    return render(request, template, context)


@login_required
def orders_status(request):
    """
    Function to site owner / admin see order status list.
    """
    orders = Order.objects.all().order_by("-date")
    form = OrderStatusForm()

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can view this page.')
        return redirect(reverse('home'))

    context = {
        'orders': orders,
        'form': form,
    }

    return render(request, 'management/admin_status.html', context)


@login_required
def update_status(request, pk):
    """
    A view to admin / site owner update order status
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        form = OrderStatusForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request,
                             f'Success. {order.order_number} status updated')
            return redirect(reverse('orders_status'))
        else:
            messages.error(request, 'Failed to update order.')
    else:
        form = OrderStatusForm(instance=order_number)

    template = 'management/admin_status.html'
    context = {
        'form': form,
        'order': order,
    }

    return render(request, template, context)
