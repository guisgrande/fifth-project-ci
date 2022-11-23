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

I ran tests using DevTools to verify that the website was responsive on multiple screen sizes. On all these devices listed below the website responded properly.

   - Mobile: Iphone XR, Iphone SE, Nexus 4, Nexus 5, Moto G4, LG Optimus L70, Galaxy S8. Pixel 2, Pixel 5.

   - Tablet: Ipad Air, Ipad Mini, Galaxy Tab S4.

   - Desktop and Laptops: 13', 15', 21' and 23'.

<details>
    <summary>Screenshots from DevTolls (Chrome) - Iphone XR</summary>
</details> 

<details>
    <summary>Screenshots from DevTolls (Chrome) - Ipad Air</summary>
</details>

The website worked correctly in Chrome, Firefox, Edge browsers in the desktop tests. It also worked correctly in tests using Safari on the iPhone.

<details>
    <summary>Screenshots from Firefox and Edge browsers</summary>
</details>

## Performance Testing

Testing done using Lighthouse DevTools to check and test Performance, Accessibility, Best Practices and SEO.

<details>
    <summary>Screenshots from Lighthouse DevTools result pages</summary>
    <div align="center">
        Home page
    </div>
    <div align="center">
        PRINT HERE
    </div>
    <div align="center">
        Products page
    </div>
    <div align="center">
        PRINT HERE
    </div>
    <div align="center">
        Product Details page
    </div>
    <div align="center">
        PRINT HERE
    </div>
    <div align="center">
        Shopbag page
    </div>
    <div align="center">
        PRINT HERE
    </div>
    <div align="center">
        Checkout page
    </div>
    <div align="center">
        PRINT HERE
    </div>
    <div align="center">
        Chekout Success page
    </div>
    <div align="center">
        PRINT HERE
    </div>
    <div align="center">
        Sign in page
    </div>
    <div align="center">
        PRINT HERE
    </div>
    <div align="center">
        Sign up page
    </div>
    <div align="center">
        PRINT HERE
    </div>
    <div align="center">
        Sign out page
    </div>
    <div align="center">
        PRINT HERE
    </div>
    <div align="center">
        Profile page
    </div>
    <div align="center">
        PRINT HERE
    </div>
    <div align="center">
        Orders page
    </div>
    <div align="center">
        PRINT HERE
    </div>
    <div align="center">
        Order Details page
    </div>
    <div align="center">
        PRINT HERE
    </div>
</details>

## Acessibility Testing

Accessibility test carried out using the [Wave Tool](https://wave.webaim.org/)
The tool showed that some elements were missing aria-label, the action was taken and corrected. When I checked the pages after the corrections, I did not identify any more significant errors.

Only on the home page it still indicates lack of contrast in the hero carousel texts, however the visibility and readability are acceptable even on mobile.

## User Story Testing

Checked each user story, with the intention of analyzing if it meets the requirement.

   - `User Story 1`: As an user, I want to know what kind of products I will find in the store, so I can decide if it is the product of my interest.
   - `Outcome`: When the user first visits the webpage store, it is possible see the products at the top of the home page, and it is also in the description of the e-commerce
   - `Result`: __Passed__

---

   - `User Story 2`: As an user, I want to see which products are on sale, so I can add them to my bag if the price attracts me.
   - `Outcome`: When the user first visits the webpage store, it is possible to see the prices of the products on offer and a tag showing the offer and discount (%) 
   - `Result`: __Passed__

---

   - `User Story 3`: As an user, I want to easily add or remove products from my bag, so I can adapt my product selection according to my needs.
   - `Outcome`: When the user access the webpage store, it is possible to add products by card container product (home page, products page) or product details and accessing the shopbag it's possible to change the quantity or remove  the product if needed.
   - `Result`: __Passed__

---

   - `User Story 4`: As an user, I want to easily proceed to the checkout when I finalize my choice, so I can complete the purchase without complications.
   - `Outcome`: When the user finishes choosing the products, it is possible to proceed to the checkout by clicking on the corresponding button (SECURE CHECKOUT) at the bottom of the shopbag page or through the messages (toasts) when modifying the bag.
   - `Result`: __Passed__

---

   - `User Story 5`: As an user, I want to see that my order has been successfully completed, so I can be sure that the payment proceeded correctly.
   - `Outcome`: When the user makes the payment and it is successfully processed, he is redirected to the order success page where he can see the order information and a confirmation order number. Also an order confirmation email is sent to the entered email address.
   - `Result`: __Passed__

---

   - `User Story 6`: As an user, I want to register or connect with the company, so I can be informed with the news and promotions.
   - `Outcome`: When the user visits the page, on the home page it is possible to see a call to the News Letter subscription and to the store's social networks links, which are also present in the footer.
   - `Result`: __Passed__

---

   - `User Story 7`: As a site owner, I want to easily add, edit or remove products, so I can provide new products or correct some information.
   - `Outcome`: When the site owner is logged in, the management options are visible where it is possible to add a new product through the form. And when entering each product an edit and delete button will be visible at the bottom of the page.
   - `Result`: __Passed__

---

   - `User Story 8`: As a site owner, I want to send a communication to the subscribers of the site, so I can send promotions and communications.
   - `Outcome`: When the owner of the site is logged in, the management options are visible where it is possible to access the News Letter page which shows a form with the subject and body for sending the e-mail to all subscribers. At the top you can see how many e-mails are subscribed.
   - `Result`: __Passed__

---

   - `User Story 9`: As a site owner, I I want to update stock and order status, so I can keep accurate information.
   - `Outcome`: When the site owner is logged in, the management options are visible where it is possible to access the Stock page and the Order Status page where it is possible to update the appropriate information for each (Quantity for each product and Status for each order).
   - `Result`: __Passed__

## Manual Testing

### Navigation bar

|   Element    | Authentication Status |   Action  |  Expected Result |   Outcome   |
|    ---    |   ---  |  ---  |   ---   |   ---   |
|    Navbar links    |   Not logged  |  Display  |   Show the following links - `Home / Shop(Drop* All Products - Categories - Offers) / Signin / Signup`   |   __`Pass`__   |
|    Navbar links    |   User logged  |  Display  |   Show the following links - `Home / Shop(Drop* All Products - Categories - Offers) / My Account(Drop* My Profile - Logout)`   |   __`Pass`__   |
|    Navbar links    |   Superuser logged  |  Display  |   Show the following links - `Home / Shop(Drop* All Products - Categories - Offers) / Management(Drop* Product - Stock - Order Status - News Letter) / My Account(Drop* My Profile - Logout)`   |   __`Pass`__   |
|    Navbar links    |   All  |  Hover  |   Hover effect on links when mouseover or clicked (mobile)   |   __`Pass`__   |
|    Navbar logo    |   All  |  Click  |   Redirect to the homepage   |   __`Pass`__   |
|    Link - Home    |   All  |  Click  |   Redirect to the homepage   |   __`Pass`__   |
|    Link - Shop    |   All  |  Click  |   Show dropdown menu list   |   __`Pass`__   |
|    Link - (Shop) All products    |   All  |  Click  |   Redirect to the products page and show all products   |   __`Pass`__   |
|    Link - (Shop) Category: Skateboard    |   All  |  Click  |   Redirect to the products page and show all skateboards   |   __`Pass`__   |
|    Link - (Shop) Category: Caps & Hats    |   All  |  Click  |   Redirect to the products page and show all caps & hats   |   __`Pass`__   |
|    Link - (Shop) Category: Backpacks & Bags    |   All  |  Click  |   Redirect to the products page and show all backpacks & bags   |   __`Pass`__   |
|    Link - (Shop) Offer: New Arrivals    |   All  |  Click  |   Redirect to the products page and show all new arrivals offer products   |   __`Pass`__   |
|    Link - (Shop) Offer: Special Sale    |   All  |  Click  |   Redirect to the products page and show all special sale offer products   |   __`Pass`__   |
|    Link - (Shop) Offer: Last Chance    |   All  |  Click  |   Redirect to the products page and show all last chance offer products   |   __`Pass`__   |
|    Link - Sign in    |   Not logged  |  Click  |   Redirect to the login page   |   __`Pass`__   |
|    Link - Sign up    |   Not logged  |  Click  |   Redirect to the register page   |   __`Pass`__   |
|    Link - My account    |   Superuser or User logged  |  Click  |   Show dropdown menu list   |   __`Pass`__   |
|    Link - (My account) My Profile    |   Superuser or User logged  |  Click  |   Redirect to the My Profile page   |   __`Pass`__   |
|    Link - (My account) Logout   |   Superuser or User logged  |  Click  |   Redirect to the logout page   |   __`Pass`__   |
|    Link - Management    |   Superuser logged  |  Click  |   Show dropdown menu list   |   __`Pass`__   |
|    Link - (Management) Product Manag.   |   Superuser logged  |  Click  |   Redirect to the Add product page   |   __`Pass`__   |
|    Link - (Management) Stock Manag.   |   Superuser logged  |  Click  |   Redirect to the Stock management page   |   __`Pass`__   |
|    Link - (Management) Order Status Manag.   |   Superuser logged  |  Click  |   Redirect to the Order Status management page   |   __`Pass`__   |
|    Link - (Management) News Letter Manag.   |   Superuser logged  |  Click  |   Redirect to the News Letter send e-mail page   |   __`Pass`__   |
|    Shopbag    |   All  |  Display  |    Show in every page, display order total and total products quantity   |   __`Pass`__   |
|    Shopbag    |   All  |  Click  |    Redirect to the shopbag page   |   __`Pass`__   |
|    Search bar    |   All  |  Display  |    Show input field to insert search query   |   __`Pass`__   |
|    Search bar    |   All  |  Click  |    Redirect to products page and display just show products that match the search   |   __`Pass`__   |

### Footer

|   Element    | Authentication Status |   Action  |  Expected Result |   Outcome   |
|    ---    |   ---  |  ---  |   ---   |   ---   |
|    Footer    |   All  |  Display  |   Show the footer links + News Letter button + Social links   |   __`Pass`__   |
|    Footer links    |   All  |  Hover  |   Hover effect on links when mouseover or clicked (mobile)   |   __`Pass`__   |
|    Social links    |   All  |  Hover  |   Hover effect on links when mouseover or clicked (mobile)   |   __`Pass`__   |
|    Footer links    |   Not logged  |  Display  |   Show the following links - `Home / All Products / Signin / Signup`   |   __`Pass`__   |
|    Footer links    |   Superuser or User logged  |  Display  |   Show the following links - `Home / All Products / My Profile / Logout`   |   __`Pass`__   |
|    Link - Home    |   All  |  Click  |   Redirect to the homepage   |   __`Pass`__   |
|    Link - All Products    |   All  |  Click  |   Redirect to the products page and show all products   |   __`Pass`__   |
|    Link - Sign in    |   Not logged  |  Click  |   Redirect to the login page   |   __`Pass`__   |
|    Link - Sign up    |   Not logged  |  Click  |   Redirect to the register page   |   __`Pass`__   |
|    Link - My Profile    |   Superuser or User logged  |  Click  |   Redirect to the My Profile page   |   __`Pass`__   |
|    Link - Logout   |   Superuser or User logged  |  Click  |   Redirect to the logout page   |   __`Pass`__   |
|    News Letter - Subscribe    |   All  |  Display  |   Open a modal box with a form (E-mail and Name) to subscribe   |   __`Pass`__   |
|    News Letter - Modal    |   All  |  Form - Click `X` |   Close the modal window    |   __`Pass`__   |
|    News Letter - Modal    |   All  |  Form - Click `Close` |   Close the modal window    |   __`Pass`__   |
|    News Letter - Modal    |   All  |  Form - Click `Subscribe` |   If input information is not correct - return a message to insert the correct information type    |   __`Pass`__   |
|    News Letter - Modal    |   All  |  Form - Click `Subscribe` |   If input information is correct and not subscribed yet - adds the information to the list and returns a success message    |   __`Pass`__   |
|    News Letter - Modal    |   All  |  Form - Click `Subscribe` |   If input information is correct and e-mail is subscribed - close modal and display message the e-mail is already subscribed    |   __`Pass`__   |
|    Social links - Facebook    |   All  |  Click  |   Open in a new window the Facebook Street Craft page   |   __`Pass`__   |
|    Social links - Instagram    |   All  |  Click  |   Open in a new window the Instagram page   |   __`Pass`__   |
|    Social links - TikTok    |   All  |  Click  |   Open in a new window the TikTok page   |   __`Pass`__   |
|    Social links - Youtube    |   All  |  Click  |   Open in a new window the Youtube page   |   __`Pass`__   |

### Home page

|   Element    | Authentication Status |   Action  |  Expected Result |   Outcome   |
|    ---    |   ---  |  ---  |   ---   |   ---   |
|    Hero section    |   All  |  Display  |   Display image carousel cointainer (3 images), text and buttons   |   __`Pass`__   |
|    New Arrivals section    |   All  |  Display  |   Display New Arrivals section with title, paragraph, shop button and 4 products cards (New Arrivals offer)  |   __`Pass`__   |
|    Special Offers section    |   All  |  Display  |   Display Special Offers section with title, paragraph, shop button and 4 products cards (Special Offers)  |   __`Pass`__   |
|    News Letter / Social section    |   All  |  Display  |   Display News Letter subscribe container form fields and subscribe button / Display social links container and a link for each social page.   |   __`Pass`__   |
|    Last Chance section    |   All  |  Display  |   Display Last Chance section with title, paragraph, shop button and 4 products cards (Last opportunity Offers)  |   __`Pass`__   |
|    Sign up section    |   Not logged  |  Display  |   Display call text for discount coupon and a button   |   __`Pass`__   |
|    Hero section - Left arrow    |   All  |  Click  |   Back to previous slide   |   __`Pass`__   |
|    Hero section - Right arrow    |   All  |  Click  |   Go to next slide   |   __`Pass`__   |
|    Hero section - Firs slide button    |   All  |  Click  |   Redirect to the products page and show all products   |   __`Pass`__   |
|    Hero section - Second slide button   |   All  |  Click  |   Redirect to the sign up page   |   __`Pass`__   |
|    Hero section - Third slide button   |   All  |  Click  |   Redirect to the products page and show all skateboards   |   __`Pass`__   |
|    New Arrivals - Shop button    |   All  |  Click  |  Redirect to the products page and show all new arrivals offer products   |   __`Pass`__   |
|    New Arrivals - Product card    |   All  |  Display  |   Show the product image, name, price, stock, quantity, less and plus buttons and ADD button.   |   __`Pass`__   |
|    New Arrivals - Product card quantity    |   All  |  Input  |  Number field accepts the value between 1 and 99 and only numbers   |   __`Pass`__   |
|    New Arrivals - Product card less button    |   All  |  Click  |  Decreases the quantity of the product (input) to a limit of at least one unit   |   __`Pass`__   |
|    New Arrivals - Product card plus button    |   All  |  Click  |  Increases the quantity of the product (input) to a maximum of 99 units   |   __`Pass`__   |
|    New Arrivals - Product card ADD button    |   All  |  Click  |  Adds the selected product and quantity to the shopbag and returns a success message    |   __`Pass`__   |
|    Special Offers - Shop button    |   All  |  Click  |  Redirect to the products page and show all special sale offer products   |   __`Pass`__   |
|    Special Offers - Product card    |   All  |  Display  |   Show the product image, name, price, stock, quantity, less and plus buttons and ADD button.   |   __`Pass`__   |
|    Special Offers - Product card quantity    |   All  |  Input  |  Number field accepts the value between 1 and 99 and only numbers   |   __`Pass`__   |
|    Special Offers - Product card less button    |   All  |  Click  |  Decreases the quantity of the product (input) to a limit of at least one unit   |   __`Pass`__   |
|    Special Offers - Product card plus button    |   All  |  Click  |  Increases the quantity of the product (input) to a maximum of 99 units   |   __`Pass`__   |
|    Special Offers - Product card ADD button    |   All  |  Click  |  Adds the selected product and quantity to the shopbag and returns a success message    |   __`Pass`__   |
|    Last Chance - Shop button    |   All  |  Click  |  Redirect to the products page and show all last opportunity offer products   |   __`Pass`__   |
|    Last Chance - Product card    |   All  |  Display  |   Show the product image, name, price, stock, quantity, less and plus buttons and ADD button.   |   __`Pass`__   |
|    Last Chance - Product card quantity    |   All  |  Input  |  Number field accepts the value between 1 and 99 and only numbers   |   __`Pass`__   |
|    Last Chance - Product card less button    |   All  |  Click  |  Decreases the quantity of the product (input) to a limit of at least one unit   |   __`Pass`__   |
|    Last Chance - Product card plus button    |   All  |  Click  |  Increases the quantity of the product (input) to a maximum of 99 units   |   __`Pass`__   |
|    Last Chance - Product card ADD button    |   All  |  Click  |  Adds the selected product and quantity to the shopbag and returns a success message    |   __`Pass`__   |
|    Any Product - Stock   |   All  |  Add to bag  |   If more than available stock, add just maximum stock available    |   __`Pass`__   |
|    Any Product - Stock   |   All  |  Add to bag  |   If less or equal than available stock, add just selected quantity    |   __`Pass`__   |
|    Any Product - Offer   |   All  |  Display  |   If the product is on offer, show the tag in the image and the old and new price (after discount).    |   __`Pass`__   |
|    News Letter - Subscribe button   |   All  |  Form - Click  |   If input information is not correct - return a message to insert the correct information type    |   __`Pass`__   |
|    News Letter - Subscribe button   |   All  |  Form - Click |   If input information is correct and not subscribed yet - adds the information to the list and returns a success message    |   __`Pass`__   |
|    News Letter - Subscribe button   |   All  |  Form - Click |   If input information is correct and e-mail is subscribed - close modal and display message the e-mail is already subscribed    |   __`Pass`__   |
|    Social - Facebook link button   |   All  |  Click  |   Open in a new window the Facebook Street Craft page   |   __`Pass`__   |
|    Social - Instagram link button   |   All  |  Click  |   Open in a new window the Instagram page   |   __`Pass`__   |
|    Social - TikTok link button   |   All  |  Click  |   Open in a new window the TikTok page   |   __`Pass`__   |
|    Social - Youtube link button   |   All  |  Click  |   Open in a new window the Youtube page   |   __`Pass`__   |
|    Sign up section - button    |   Not logged  |  Click  |   Redirect to the sign up page   |   __`Pass`__   |

### Products page

|   Element    | Authentication Status |   Action  |  Expected Result |   Outcome   |
|    ---    |   ---  |  ---  |   ---   |   ---   |
|    Total products    |   All  |  Display  |   Show text informing the total of products   |   __`Pass`__   |
|    Sort all products by    |   All  |  Display  |   Show sort selection box field with four options: `By price: low to high` / `By price: high to low` / `By name: A to Z` / `By name: Z to A`  |   __`Pass`__   |
|    Products    |   All  |  Display  |   Show the total of 8 products per page   |   __`Pass`__   |
|    Pagination    |   All  |  Display  |   Show the number of pages, buttons to navigate between them ade the number of produts showing at current page   |   __`Pass`__   |
|    Pagination - First button    |   All  |  Click  |   Load the first page of product results  |   __`Pass`__   |
|    Pagination - Last button  |   All  |  Click  |   Load the last page available of product results  |   __`Pass`__   |
|    Pagination - `<<` previous button   |   All  |  Click  |   Load the previous available page of product results |   __`Pass`__   |
|    Pagination - `>>` next button   |   All  |  Click  |   Load the next available page of product results  |   __`Pass`__   |
|    Product card    |   All  |  Display  |   Show the product image, name, price, stock, quantity, less and plus buttons and ADD button.   |   __`Pass`__   |
|    Product card - Offer   |   All  |  Display  |   If the product is on offer, show the tag in the image and the old and new price (after discount).    |   __`Pass`__   |
|    Product card quantity    |   All  |  Input  |  Number field accepts the value between 1 and 99 and only numbers   |   __`Pass`__   |
|    Product card less button    |   All  |  Click  |  Decreases the quantity of the product (input) to a limit of at least one unit   |   __`Pass`__   |
|    Product card plus button    |   All  |  Click  |  Increases the quantity of the product (input) to a maximum of 99 units   |   __`Pass`__   |
|    Product card ADD button    |   All  |  Click  |  Adds the selected product and quantity to the shopbag and returns a success message    |   __`Pass`__   |
|    Product - Stock   |   All  |  Add to bag  |   If more than available stock, add just maximum stock available    |   __`Pass`__   |
|    Product - Stock   |   All  |  Add to bag  |   If less or equal than available stock, add just selected quantity    |   __`Pass`__   |
|    Product card image    |   All  |  Click  |  Redirect to that product details page   |   __`Pass`__   |
|    Sort all products - `By price: low to high`    |   All  |  Select - Click  |   Reload page and display all products ordered by price from cheapest to most expensive   |   __`Pass`__   |
|    Sort all products - `By price: high to low`    |   All  |  Select - Click  |   Reload page and display all products ordered by price from the most expensive to the cheapest   |   __`Pass`__   |
|    Sort all products - `By name: A to Z`    |   All  |  Select - Click  |   Reload page and display all products sorted in alphabetical order from A to Z    |   __`Pass`__   |
|    Sort all products - `By name: Z to A`    |   All  |  Select - Click  |   Reload page and display all products sorted in alphabetical order from Z to A    |   __`Pass`__   |

### Product details page

|   Element    | Authentication Status |   Action  |  Expected Result |   Outcome   |
|    ---    |   ---  |  ---  |   ---   |   ---   |
|    Product details    |   All  |  Display  |   Show the product image, reviews section, name, SKU, price, stock, quantity, less and plus buttons, Keep Shoping and Add to bag buttons, product description   |   __`Pass`__   |
|    Product details - Offer   |   All  |  Display  |   If the product is on offer, show the tag in the image and the old and new price (after discount).    |   __`Pass`__   |
|    Product details - Reviews avarage score    |   All  |  Display  |   Show the average score of all reviews   |   __`Pass`__   |
|    Product details - `Reviews` button   |   Not logged  |  Display  |   Show the just span with total of reviews for the product   |   __`Pass`__   |
|    Product details - `Reviews` button   |   Superuser or User logged  |  Display  |   Show a button with total of reviews for the product   |   __`Pass`__   |
|    Product details - `Reviews` button   |   Superuser or User logged  |  Click  |   Redirect to review product page   |   __`Pass`__   |
|    Product details - Stock   |   All  |  Display  |   Show the available quantity for the product    |   __`Pass`__   |
|    Product details - Stock   |   All  |  Add to bag  |   If more than available stock, add just maximum stock available    |   __`Pass`__   |
|    Product details - Stock   |   All  |  Add to bag  |   If less or equal than available stock, add just selected quantity    |   __`Pass`__   |
|    Product details - `KEEP SHOPPING` button   |   All  |  Click  |   Redirect to review product page   |   __`Pass`__   |
|    Product details - `ADD TO BAG` button   |   All  |  Click  |   Adds the selected product and quantity to the shopbag and returns a success message   |   __`Pass`__   |

### Product reviews page

|   Element    | Authentication Status |   Action  |  Expected Result |   Outcome   |
|    ---    |   ---  |  ---  |   ---   |   ---   |
|    Product reviews    |   Superuser or User logged  |  Display  |   Show the product image, name, back to product button, reviews avarage and total reviews, list of all reviews   |   __`Pass`__   |
|    Product reviews    |   Not logged  |  Display  |   Dont't load the page, redirect to sign in page and return a error message   |   __`Pass`__   |
|    Product reviews - form    |   Superuser or User logged  |  Display  |   If the user did not buy the product, do not show the form to review   |   __`Pass`__   |
|    Product reviews - form    |   Superuser or User logged  |  Display  |   If the user bought the product and has already reviewed it, do not show the form. Show text informing that already reviewed.   |   __`Pass`__   |
|    Product reviews - form    |   Superuser or User logged  |  Display  |   If the user bought the product and has not reviewed it yet, show the form.   |   __`Pass`__   |
|    Product reviews - form    |   Superuser or User logged  |  Select - Click  |   Highlight the user's selection among the available options to make clear which one will be assigned   |   __`Pass`__   |
|    Product reviews - form `Review` button    |   Superuser or User logged  |  Click  |   Submits the user's vote and returns the message that the review was completed. Reloads the page and updates the new review.   |   __`Pass`__   |
|    Product reviews - `Back to porduct` button    |   Superuser or User logged  |  Click  |   Redirect (return) to product details page   |   __`Pass`__   |

### Sign in page

|   Element    | Authentication Status |   Action  |  Expected Result |   Outcome   |
|    ---    |   ---  |  ---  |   ---   |   ---   |
|    Signin page    |   Superuser or User logged  |   Display  |   Don't load page, redirect to home page.   |   Pass   |
|    Signin page    |   Not logged  |   Display  |   Display Login using your social account: `Google acount`   |   Pass   |
|    Signin page    |   Not logged  |   Display  |   Display the following fields inside the form - `Username/E-mail, Password`   |   Pass   |
|    Signin page    |   Not logged  |   Display  |   Display  `Signin` button   |   Pass   |
|    Signin page    |   Not logged  |   Display  |   Display  `Forgot Password` button   |   Pass   |
|    Signin page    |   Not logged  |   Display  |   Display  `Remember Me` check element   |   Pass   |
|    Signin page    |   Not logged  |   Display  |   Show calling text for those who aren't registered and `Signup` button  |   Pass   |
|    Signin form    |   Not logged  |   Field Username or e-mail: empty  |   Submitting: Form not submitted. Warning message  |   Pass   |
|    Signin form    |   Not logged  |   Field Username or e-mail: wrong username or e-mail  |   Submitting: Form not submitted. Warning message  |   Pass   |
|    Signin form    |   Not logged  |   Field Username or e-mail: correct username or e-mail  |   Submitting: Form submitted. Success message  |   Pass   |
|    Signin form    |   Not logged  |   Field Password: empty  |   Submitting: Form not submitted. Warning message  |   Pass   |
|    Signin form    |   Not logged  |   Field Password: wrong password  |   Submitting: Form not submitted. Warning message  |   Pass   |
|    Signin form    |   Not logged  |   Field Password: correct password  |   Submitting: Form submitted. Success message  |   Pass   |
|    Signin Goggle button    |   Not logged  |   Click  |   Load Google OAuth access page    |   Pass*   |
|    Signin button    |   Not logged  |   Click  |   If form valid - User authenticated login, redirects to home page, shows success message    |   Pass   |
|    Signup button    |   Not logged  |   Click  |   Redirect to the Signup page (Register)    |   Pass   |
|    Forgot Password button    |   Not logged  |   Click  |   Redirect Forgot password page    |   Pass   |
|    Remember me    |   Not logged  |   Check  |   If the user logs into an existing account and confirms the selection, it saves the password in the browser.    |   Pass   |

Observation: Access using the Google account is not working 100% of the time. Sometimes it returns error 400: redirec_uri_mismatch

### Forgot password page

|   Element    | Authentication Status |   Action  |  Expected Result |   Outcome   |
|    ---    |   ---  |  ---  |   ---   |   ---   |
|    Password Reset page    |   All  |   Display  |   Display the following text `Forgotten your password? Enter your e-mail address below, and we'll send you an e-mail allowing you to reset it`   |   Pass   |
|    Password Reset page    |   Superuser or User logged  |   Display  |   Display the following extra text `Note: you are already logged in as ...`   |   Pass   |
|    Password Reset page    |   All  |   Display  |   Display  `Sign out` button   |   Pass   |
|    `Reset My Password` button    |   All  |   Click  |   If the e-mail is not in correct format, don't proceed and inform that the format is wrong    |   Pass   |
|    `Reset My Password` button    |   All  |   Click  |   If the e-mail is not registered, return message: `The e-mail address is not assigned to any user account`    |   Pass   |
|    `Reset My Password` button    |   All  |   Click  |   If the e-mail is registered, proceed and send an e-mail with change password link   |   Pass   |
|    Change password page    |   All  |   Display  |   Accessed by the e-mail link, it shows two fields for a new password and the `change password` button   |   Pass   |
|    Change password page - button   |   All  |   Click  |   If the two password fields are not identical, it returns the message that it must be corrected   |   Pass   |
|    Change password page - button   |   All  |   Click  |   If the two password fields are identical, change the password and show a message of success   |   Pass   |

### Sign up page

|   Element    | Authentication Status |   Action  |  Expected Result |   Outcome   |
|    ---    |   ---  |  ---  |   ---   |   ---   |
|    Signup page    |   Superuser or User logged  |   Display  |   Don't load page, redirect to home page.   |   Pass   |
|    Signup page    |   Not logged  |   Display  |   Display the following fields inside the form - `E-mail, E-mail (again),Username, Password, Password (again)`   |   Pass   |
|    Signup page    |   Not logged  |   Display  |   Display  `Signup` button   |   Pass   |
|    Signup page    |   Not logged  |   Display  |   Show calling text for those who are already registered and `Signin` button  |   Pass   |
|    Signup form    |   Not logged  |   Field Username: empty  |   Submitting: Form not submitted. Warning message  |   Pass   |
|    Signup form    |   Not logged  |   Field Username: duplicated  |   Submitting: Form not submitted. Warning message  |   Pass   |
|    Signup form    |   Not logged  |   Field Username: incorrect format  |   Submitting: Form not submitted. Warning message  |   Pass   |
|    Signup form    |   Not logged  |   Field Username: correct format  |   Submitting: Form submitted. Success message  |   Pass   |
|    Signup form    |   Not logged  |   Field E-mail: empty  |   Submitting: Form submitted. Success message |   Pass   |
|    Signup form    |   Not logged  |   Field E-mail: duplicated  |   Submitting: Form not submitted. Warning message |   Pass   |
|    Signup form    |   Not logged  |   Field E-mail: incorrect format  |   Submitting: Form not submitted. Warning message |   Pass   |
|    Signup form    |   Not logged  |   Field E-mail (again): empty  |   Submitting: Form not submitted. Warning message |   Pass   |
|    Signup form    |   Not logged  |   Field E-mail (again): incorrect format  |   Submitting: Form not submitted. Warning message |   Pass   |
|    Signup form    |   Not logged  |   Field E-mail (again): correct format |   Submitting: Form submitted. Success message |   Pass   |
|    Signup form    |   Not logged  |   Field E-mail: correct format match  |   Submitting: Form submitted. Success message |   Pass   |
|    Signup form    |   Not logged  |   Field Password: empty  |   Submitting: Form not submitted. Warning message  |   Pass   |
|    Signup form    |   Not logged  |   Field Password: incorrect format  |   Submitting: Form not submitted. Warning message  |   Pass   |
|    Signup form    |   Not logged  |   Field Password: correct format  |   Submitting: Form submitted. Success message  |   Pass   |
|    Signup form    |   Not logged  |   Field Password (again): empty  |   Submitting: Form not submitted. Warning message |   Pass   |
|    Signup form    |   Not logged  |   Field Password (again): incorrect format  |   Submitting: Form not submitted. Warning message |   Pass   |
|    Signup form    |   Not logged  |   Field Password (again): correct format match |   Submitting: Form submitted. Success message |   Pass   |
|    Signup form    |   Not logged  |   Fields Password + Password (again): don't match |   Submitting: Form not submitted. Warning message |   Pass   |
|    Signup form    |   Not logged  |   Fields Password + Password (again): match |   Submitting: Form submitted. Success message |   Pass   |
|    Signup button    |   Not logged  |   Click  |   If form valid - Adds new user, redirects to home page, shows success message    |   Pass   |
|    Signin button    |   Not logged  |   Click  |   Redirect to the Signin page (Login)    |   Pass   |

### Sign out page

|   Element    | Authentication Status |   Action  |  Expected Result |   Outcome   |
|    ---    |   ---  |  ---  |   ---   |   ---   |
|    Logout page    |   Not logged  |   Display  |   Dont't load the page, redirect to sign in page   |   Pass   |
|    Logout page    |   Superuser or User logged  |   Display  |   Display the following text inside the form - `Are you sure you want to sign out?`   |   Pass   |
|    Logout page    |   Superuser or User logged  |   Display  |   Display  `Sign out` button   |   Pass   |
|    Signout button    |   Superuser or User logged  |   Click  |   Logout the user, redirects to home page, shows success message    |   Pass   |

### My Profile page

|   Element    | Authentication Status |   Action  |  Expected Result |   Outcome   |
|    ---    |   ---  |  ---  |   ---   |   ---   |

### My orders page

|   Element    | Authentication Status |   Action  |  Expected Result |   Outcome   |
|    ---    |   ---  |  ---  |   ---   |   ---   |

### Order details page

|   Element    | Authentication Status |   Action  |  Expected Result |   Outcome   |
|    ---    |   ---  |  ---  |   ---   |   ---   |

### Change password page

|   Element    | Authentication Status |   Action  |  Expected Result |   Outcome   |
|    ---    |   ---  |  ---  |   ---   |   ---   |

### Delete profile page

|   Element    | Authentication Status |   Action  |  Expected Result |   Outcome   |
|    ---    |   ---  |  ---  |   ---   |   ---   |

### Shopbag page

|   Element    | Authentication Status |   Action  |  Expected Result |   Outcome   |
|    ---    |   ---  |  ---  |   ---   |   ---   |

### Checkout page

|   Element    | Authentication Status |   Action  |  Expected Result |   Outcome   |
|    ---    |   ---  |  ---  |   ---   |   ---   |

### Checkout Success page

|   Element    | Authentication Status |   Action  |  Expected Result |   Outcome   |
|    ---    |   ---  |  ---  |   ---   |   ---   |
