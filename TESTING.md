# Street Craft - Testing

<details>
    <summary>Summary</summary>

- [Validation](#validation).

- [Responsiveness and Browser Compability Testing](#responsiveness-and-browser-compability-testing).
 
- [Performance Testing](#performance-testing).
 
- [Acessibility Testing](#acessibility-testing).
  
- [User Story Testing](#user-story-testing).

- [Manual Testing](#manual-testing).
 
</details> 

## Validation

Here is a report of the validations made on the code and their results

- __HTML__

List of pages validated by the tool [W3C Markup Validator](https://validator.w3.org/)

|   Page    |   URL  |  Result |  Link |
|    ---    |   ---  |   ---   |  ---  |
|    Home    | `https://streetcraft.herokuapp.com/` |   No errors   |  [Validated](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstreetcraft.herokuapp.com%2F)  |
|    Products    |   `https://streetcraft.herokuapp.com/all-products/`  |   No errors   |  [Validated](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fall-products%2F)  |
|    Prod. Detail    |   `https://streetcraft.herokuapp.com/details/treft-hill-skateboard/`  |   No errors   |  [Validated](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fdetails%2Ftreft-hill-skateboard%2F)  |
|    Prod. Review    |   `https://streetcraft.herokuapp.com/review-product/treft-hill-skateboard/`  |   No errors   |  [Validated](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstreetcraft.herokuapp.com%2Freview-product%2Ftreft-hill-skateboard%2F)  |
|    Login    |   `https://streetcraft.herokuapp.com/accounts/login/`  |   No errors   |  [Validated](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstreetcraft.herokuapp.com%2Faccounts%2Flogin%2F)  |
|    Register    |   `https://streetcraft.herokuapp.com/accounts/signup/`  |   No errors   |  [Validated](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstreetcraft.herokuapp.com%2Faccounts%2Fsignup%2F)  |
|    Forget Password    |   `https://streetcraft.herokuapp.com/accounts/password/reset/`  |   No errors   |  [Validated](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstreetcraft.herokuapp.com%2Faccounts%2Fpassword%2Freset%2F)  |
|    Logout    |   `https://streetcraft.herokuapp.com/accounts/logout/`  |   No errors   |  [Validated](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstreetcraft.herokuapp.com%2Faccounts%2Flogout%2F)  |
|    Profile    |   `https://streetcraft.herokuapp.com/profile/user/`  |   No errors   |  [Validated](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fprofile%2Fuser%2F)  |
|    My Orders    |   `https://streetcraft.herokuapp.com/profile/my-orders/`  |   No errors   |  [Validated](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fprofile%2Fmy-orders%2F)  |
|    Order Detail    |   `https://streetcraft.herokuapp.com/profile/order/40ED900E3DBC42B5B120E7A1153916D9`  |   No errors   |  [Validated](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fprofile%2Forder%2F40ED900E3DBC42B5B120E7A1153916D9)  |
|    Change Password    |   `https://streetcraft.herokuapp.com/accounts/password/change/`  |   No errors   |  [Validated](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstreetcraft.herokuapp.com%2Faccounts%2Fpassword%2Fchange%2F)  |
|    Delete Profile    |   `https://streetcraft.herokuapp.com/profile/delete-profile/`  |   No errors   |  [Validated](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fprofile%2Fdelete-profile%2F)  |
|    Shopbag    |   `https://streetcraft.herokuapp.com/shop/bag/`  |   No errors   |  [Validated](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fshop%2Fbag%2F)  |
|    Checkout    |   `https://streetcraft.herokuapp.com/checkout/order/`  |   No errors   |  [Validated](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fcheckout%2Forder%2F)  |
|    Checkout Success    |   `https://streetcraft.herokuapp.com/checkout/order-success/40ED900E3DBC42B5B120E7A1153916D9`  |   No errors   |  [Validated](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fcheckout%2Forder-success%2F40ED900E3DBC42B5B120E7A1153916D9)  |
|    Manag. Add product    |   `https://streetcraft.herokuapp.com/management/add-product/`  |   No errors   |  [Validated](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fmanagement%2Fadd-product%2F)  |
|    Manag. Edit product    |   `https://streetcraft.herokuapp.com/management/edit-product/treft-hill-skateboard/`  |   No errors   |  [Validated](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fmanagement%2Fedit-product%2Ftreft-hill-skateboard%2F)  |
|    Manag. Delete product    |   `https://streetcraft.herokuapp.com/management/delete-product/treft-hill-skateboard/`  |   No errors   |  [Validated](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fmanagement%2Fdelete-product%2Ftreft-hill-skateboard%2F)  |
|    Manag. Stock    |   `https://streetcraft.herokuapp.com/management/stock-control/`  |   No errors   |  [Validated](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fmanagement%2Fstock-control%2F)  |
|    Manag. Order Status    |   `https://streetcraft.herokuapp.com/management/orders-status/`  |   No errors   |  [Validated](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fmanagement%2Fstock-control%2F)  |
|    Manag. News Letter    |   `https://streetcraft.herokuapp.com/management/news-letter-mails/`  |   No errors   |  [Validated](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fmanagement%2Fnews-letter-mails%2F)  |

- __CSS__

List of pages validated an Unique CSS file validated by the tool [W3C Jigsaw Validator](https://jigsaw.w3.org/css-validator/)

|   Page    |   URL  |  Result |  Link |
|    ---    |   ---  |   ---   |  ---  |
|    Home    | `https://streetcraft.herokuapp.com/` |   No errors   |  [Validated](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fstreetcraft.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)  |
|    Products    |   `https://streetcraft.herokuapp.com/all-products/`  |   No errors   |  [Validated](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fall-products%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)  |
|    Prod. Detail    |   `https://streetcraft.herokuapp.com/details/treft-hill-skateboard/`  |   No errors   |  [Validated](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fdetails%2Ftreft-hill-skateboard%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)  |
|    Prod. Review    |   `https://streetcraft.herokuapp.com/review-product/treft-hill-skateboard/`  |   No errors   |  [Validated](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fstreetcraft.herokuapp.com%2Freview-product%2Ftreft-hill-skateboard%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)  |
|    Login    |   `https://streetcraft.herokuapp.com/accounts/login/`  |   No errors   |  [Validated](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fstreetcraft.herokuapp.com%2Faccounts%2Flogin%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)  |
|    Register    |   `https://streetcraft.herokuapp.com/accounts/signup/`  |   No errors   |  [Validated](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fstreetcraft.herokuapp.com%2Faccounts%2Fsignup%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)  |
|    Forget Password    |   `https://streetcraft.herokuapp.com/accounts/password/reset/`  |   No errors   |  [Validated](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fstreetcraft.herokuapp.com%2Faccounts%2Fpassword%2Freset%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)  |
|    Logout    |   `https://streetcraft.herokuapp.com/accounts/logout/`  |   No errors   |  [Validated](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fstreetcraft.herokuapp.com%2Faccounts%2Flogout%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)  |
|    Profile    |   `https://streetcraft.herokuapp.com/profile/user/`  |   No errors   |  [Validated](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fprofile%2Fuser%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)  |
|    My Orders    |   `https://streetcraft.herokuapp.com/profile/my-orders/`  |   No errors   |  [Validated](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fprofile%2Fmy-orders%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)  |
|    Order Detail    |   `https://streetcraft.herokuapp.com/profile/order/40ED900E3DBC42B5B120E7A1153916D9`  |   No errors   |  [Validated](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fprofile%2Forder%2F40ED900E3DBC42B5B120E7A1153916D9&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)  |
|    Change Password    |   `https://streetcraft.herokuapp.com/accounts/password/change/`  |   No errors   |  [Validated](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fstreetcraft.herokuapp.com%2Faccounts%2Fpassword%2Fchange%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)  |
|    Delete Profile    |   `https://streetcraft.herokuapp.com/profile/delete-profile/`  |   No errors   |  [Validated](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fprofile%2Fdelete-profile%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)  |
|    Shopbag    |   `https://streetcraft.herokuapp.com/shop/bag/`  |   No errors   |  [Validated](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fshop%2Fbag%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)  |
|    Checkout    |   `https://streetcraft.herokuapp.com/checkout/order/`  |   No errors   |  [Validated](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fcheckout%2Forder%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)  |
|    Checkout Success    |   `https://streetcraft.herokuapp.com/checkout/order-success/40ED900E3DBC42B5B120E7A1153916D9`  |   No errors   |  [Validated](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fcheckout%2Forder-success%2F40ED900E3DBC42B5B120E7A1153916D9&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)  |
|    Manag. Add product    |   `https://streetcraft.herokuapp.com/management/add-product/`  |   No errors   |  [Validated](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fmanagement%2Fadd-product%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)  |
|    Manag. Edit product    |   `https://streetcraft.herokuapp.com/management/edit-product/treft-hill-skateboard/`  |   No errors   |  [Validated](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fmanagement%2Fedit-product%2Ftreft-hill-skateboard%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)  |
|    Manag. Delete product    |   `https://streetcraft.herokuapp.com/management/delete-product/treft-hill-skateboard/`  |   No errors   |  [Validated](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fmanagement%2Fdelete-product%2Ftreft-hill-skateboard%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)  |
|    Manag. Stock    |   `https://streetcraft.herokuapp.com/management/stock-control/`  |   No errors   |  [Validated](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fmanagement%2Fstock-control%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)  |
|    Manag. Order Status    |   `https://streetcraft.herokuapp.com/management/orders-status/`  |   No errors   |  [Validated](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fmanagement%2Forders-status%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)  |
|    Manag. News Letter    |   `https://streetcraft.herokuapp.com/management/news-letter-mails/`  |   No errors   |  [Validated](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fstreetcraft.herokuapp.com%2Fmanagement%2Fnews-letter-mails%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)  |

- __Java Script__

List of files validated by the tool [JS Hint](https://jshint.com/)

- Script 01

```
    $(document).ready(function () {
      $('body').addClass('bg-social');
    });
```

No errors identified for this script.

<details>
    <summary>Script present in following files</summary>

| File |   File patch  |
| --- |   ---  |
| 01 |  `templates/account/login.html`  |
| 02 |  `templates/account/logout.html`  |
| 03 |  `templates/account/signup.html`  |
| 04 |  `templates/account/verification_sent.html`  |
| 05 |  `templates/account/email_confirm.html`  |
| 06 |  `templates/account/password_change.html`  |
| 07 |  `templates/account/password_reset.html`  |

</details>

<details>
    <summary>JSHint Print result</summary>
    <div align="center">
         PRINT HERE
    </div>
</details>

- Script 02

```
    (function() {
      var message = "{% trans 'Do you really want to remove the selected e-mail address?' %}";
      var actions = document.getElementsByName('action_remove');
      if (actions.length) {
        actions[0].addEventListener("click", function(e) {
          if (! confirm(message)) {
            e.preventDefault();
          }
        });
      }
    })();
```

No errors identified for this script.

<details>
    <summary>Script present in following files</summary>

| File |   File patch  |
| --- |   ---  |
| 01 |  `templates/account/email.html`  |
    
</details>

<details>
    <summary>JSHint Print result</summary>
    <div align="center">
         PRINT HERE
    </div>
</details> 

- Script 03

```
    $('.toast').toast('show');
```

No errors identified for this script.

<details>
    <summary>Script present in following files</summary>

| File |   File patch  |
| --- |   ---  |
| 01 |  `templates/base.html`  |
    
</details>

<details>
    <summary>JSHint Print result</summary>
    <div align="center">
         PRINT HERE
    </div>
</details> 

- Script 04

```
    $('.update-item').click(function(e) {
        var form = $(this).prev('.update-form');
        form.submit();
    });

    $('.remove-item').click(function(e) {
        var csrfToken = "{{ csrf_token }}";
        var itemId = $(this).attr('id').split('remove_')[1];
        var url = `/shop/remove/${itemId}/`;
        var data = {'csrfmiddlewaretoken': csrfToken};

        $.post(url, data)
         .done(function() {
             location.reload();
         });
    });
```

No errors identified for this script. One warging: __'template literal syntax' is only available in ES6 (use 'esversion: 6').__

<details>
    <summary>Script present in following files</summary>

| File |   File patch  |
| --- |   ---  |
| 01 |  `templates/shopbag/bag.html`  |
    
</details>

<details>
    <summary>JSHint Print result</summary>
    <div align="center">
         PRINT HERE
    </div>
</details> 

- Script 05

```
    // Disable +/- buttons outside 1-99 range
    function handleEnableDisable(itemId) {
        var currentValue = parseInt($(`#id_qty_${itemId}`).val());
        var minusDisabled = currentValue < 2;
        var plusDisabled = currentValue > 98;
        $(`#${itemId}-decrement-qty`).prop('disabled', minusDisabled);
        $(`#${itemId}-increment-qty`).prop('disabled', plusDisabled);
    }

    // Ensure proper enabling/disabling of all inputs on page load
    var allQtyInputs = $('.qty_input');
    for(var i = 0; i < allQtyInputs.length; i++){
        var itemId = $(allQtyInputs[i]).data('item_id');
        handleEnableDisable(itemId);
    }

    // Check enable/disable every time the input is changed
    $('.qty_input').change(function() {
        var itemId = $(this).data('item_id');
        handleEnableDisable(itemId);
    });

    // Increment quantity of products
    $('.increment-qty').click(function(e) {
       e.preventDefault();
       var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
       var currentValue = parseInt($(closestInput).val());
       $(closestInput).val(currentValue + 1);
       var itemId = $(this).data('item_id');
       handleEnableDisable(itemId);
    });

    // Decrement quantity of products
    $('.decrement-qty').click(function(e) {
       e.preventDefault();
       var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
       var currentValue = parseInt($(closestInput).val());
       $(closestInput).val(currentValue - 1);
       var itemId = $(this).data('item_id');
       handleEnableDisable(itemId);
    });
```

No errors identified for this script. Three wargings: __'template literal syntax' is only available in ES6 (use 'esversion: 6').__

<details>
    <summary>Script present in following files</summary>

| File |   File patch  |
| --- |   ---  |
| 01 |  `templates/includes/script_quantity_input.html`  |
    
</details>

<details>
    <summary>JSHint Print result</summary>
    <div align="center">
         PRINT HERE
    </div>
</details> 

- Script 06

```
    var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
    var clientSecret = $('#id_client_secret').text().slice(1, -1);
    var stripe = Stripe(stripePublicKey);
    var elements = stripe.elements();
    var style = {
        base: {
            color: '#000',
            fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
            fontSmoothing: 'antialiased',
            fontSize: '16px',
            '::placeholder': {
                color: '#aab7c4'
            }
        },
        invalid: {
            color: '#dc3545',
            iconColor: '#dc3545'
        }
    };
    var card = elements.create('card', {style: style});
    card.mount('#card-element');

    // Handle realtime validation errors on the card element
    card.addEventListener('change', function (event) {
        var errorDiv = document.getElementById('card-errors');
        if (event.error) {
            var html = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${event.error.message}</span>
            `;
            $(errorDiv).html(html);
        } else {
            errorDiv.textContent = '';
        }
    });

    // Handle form submit
    var form = document.getElementById('payment-form');

    form.addEventListener('submit', function(ev) {
        ev.preventDefault();
        card.update({ 'disabled': true});
        $('#submit-button').attr('disabled', true);
        $('#payment-form').fadeToggle(100);
        $('#loading-overlay').fadeToggle(100);

        var saveInfo = Boolean($('#id-save-info').attr('checked'));
        // From using {% csrf_token %} in the form
        var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
        var postData = {
            'csrfmiddlewaretoken': csrfToken,
            'client_secret': clientSecret,
            'save_info': saveInfo,
        };
        var url = '/checkout/cache-checkout-data/';

        $.post(url, postData).done(function () {
            stripe.confirmCardPayment(clientSecret, {
                payment_method: {
                    card: card,
                    billing_details: {
                        name: $.trim(form.full_name.value),
                        phone: $.trim(form.phone_number.value),
                        email: $.trim(form.email.value),
                        address:{
                            line1: $.trim(form.street_address1.value),
                            line2: $.trim(form.street_address2.value),
                            city: $.trim(form.town_or_city.value),
                            country: $.trim(form.country.value),
                            state: $.trim(form.county.value),
                        }
                    }
                },
                shipping: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    address: {
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        postal_code: $.trim(form.postcode.value),
                        state: $.trim(form.county.value),
                    }
                },
            }).then(function(result) {
                if (result.error) {
                    var errorDiv = document.getElementById('card-errors');
                    var html = `
                        <span class="icon" role="alert">
                        <i class="fas fa-times"></i>
                        </span>
                        <span>${result.error.message}</span>`;
                    $(errorDiv).html(html);
                    $('#payment-form').fadeToggle(100);
                    $('#loading-overlay').fadeToggle(100);
                    card.update({ 'disabled': false});
                    $('#submit-button').attr('disabled', false);
                } else {
                    if (result.paymentIntent.status === 'succeeded') {
                        form.submit();
                    }
                }
            });
        }).fail(function () {
            // just reload the page, the error will be in django messages
            location.reload();
        })
    });
```

No errors identified for this script. Two wargings: __'template literal syntax' is only available in ES6 (use 'esversion: 6').__

<details>
    <summary>Script present in following files</summary>

| File |   File patch  |
| --- |   ---  |
| 01 |  `static/js/stripe_elements.js `  |
    
</details>

<details>
    <summary>JSHint Print result</summary>
    <div align="center">
         PRINT HERE
    </div>
</details> 

- __Python__

List of pages validated by the tool [PEP8CI - By Code Institute](https://pep8ci.herokuapp.com/)

- Checkout app

|   File    |   Result |
|    ---    |    ---   |
|    `checkout/admin.py`    |   No errors   |
|    `checkout/apps.py`    |   No errors   |
|    `checkout/forms.py`    |   No errors   |
|    `checkout/models.py`    |   No errors   |
|    `checkout/signals.py `    |   No errors   |
|    `checkout/tests.py`    |   No errors   |
|    `checkout/urls.py`    |   No errors   |
|    `checkout/views.py`    |   No errors   |
|    `checkout/webhook_handler.py`    |   No errors   |
|    `checkout/webhooks.py`    |   No errors   |

<details>
    <summary>Checkout PEP8CI Print results</summary>
    <div align="center">
         PRINT HERE
    </div>
</details>

- Home app

|   File    |   Result |
|    ---    |    ---   |
|    `home/admin.py`    |   No errors   |
|    `home/apps.py`    |   No errors   |
|    `home/models.py`    |   No errors   |
|    `home/tests.py`    |   No errors   |
|    `home/urls.py`    |   No errors   |
|    `home/views.py`    |   No errors   |

<details>
    <summary>Home PEP8CI Print results</summary>
    <div align="center">
         PRINT HERE
    </div>
</details> 

- Management app

|   File    |   Result |
|    ---    |    ---   |
|    `management/admin.py`    |   No errors   |
|    `management/apps.py`    |   No errors   |
|    `management/forms.py`    |   No errors   |
|    `management/models.py`    |   No errors   |
|    `management/tests.py`    |   No errors   |
|    `management/urls.py`    |   No errors   |
|    `management/views.py`    |   No errors   |

<details>
    <summary>Management PEP8CI Print results</summary>
    <div align="center">
         PRINT HERE
    </div>
</details>

- Products app

|   File    |   Result |
|    ---    |    ---   |
|    `products/templatetags/product_tag.py`    |   No errors   |
|    `products/admin.py`    |   No errors   |
|    `products/apps.py`    |   No errors   |
|    `products/forms.py`    |   No errors   |
|    `products/models.py`    |   No errors   |
|    `products/tests.py`    |   No errors   |
|    `products/urls.py`    |   No errors   |
|    `products/views.py`    |   No errors   |

<details>
    <summary>Products PEP8CI Print results</summary>
    <div align="center">
         PRINT HERE
    </div>
</details>

- Profiles app

|   File    |   Result |
|    ---    |    ---   |
|    `profiles/admin.py`    |   No errors   |
|    `profiles/apps.py`    |   No errors   |
|    `profiles/forms.py`    |   No errors   |
|    `profiles/models.py`    |   No errors   |
|    `profiles/tests.py`    |   No errors   |
|    `profiles/urls.py`    |   No errors   |
|    `profiles/views.py`    |   No errors   |

<details>
    <summary>Profiles PEP8CI Print results</summary>
    <div align="center">
         PRINT HERE
    </div>
</details>

- Shopbag app

|   File    |   Result |
|    ---    |    ---   |
|    `shopbag/templatetags/bag_tools.py`    |   No errors   |
|    `shopbag/admin.py`    |   No errors   |
|    `shopbag/apps.py`    |   No errors   |
|    `shopbag/contexts.py `    |   No errors   |
|    `shopbag/models.py`    |   No errors   |
|    `shopbag/tests.py`    |   No errors   |
|    `shopbag/urls.py`    |   No errors   |
|    `shopbag/views.py`    |   No errors   |

<details>
    <summary>Shopbag PEP8CI Print results</summary>
    <div align="center">
         PRINT HERE
    </div>
</details>

- Streetcraft project

|   File    |   Result |
|    ---    |    ---   |
|    `streetcraft/asgi.py`    |   No errors   |
|    `streetcraft/settings.py`    |   4 line too long (E501)   |
|    `shopbag/contexts.py `    |   No errors   |
|    `streetcraft/urls.py`    |   No errors   |
|    `streetcraft/views.py`    |   No errors   |
|    `streetcraft/wsgi.py`    |   No errors   |

The four too long line errors found on settings were related to links from `AUTH_PASSWORD_VALIDATORS`. 

<details>
    <summary>Streetcraft PEP8CI Print results</summary>
    <div align="center">
         PRINT HERE
    </div>
</details>

- Extra files

|   File    |   Result |
|    ---    |    ---   |
|    `custom_storages.py`    |   No errors   |
|    `manage.py`    |   No errors   |

<details>
    <summary>Extra files PEP8CI Print results</summary>
    <div align="center">
         PRINT HERE
    </div>
</details>

## Responsiveness and Browser Compability Testing

## Performance Testing

## Acessibility Testing

Accessibility test carried out using the [Wave Tool](https://wave.webaim.org/)

## User Story Testing

## Manual Testing
