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

- __Python__

List of pages validated by the tool [PEP8](http://pep8online.com/)

## Responsiveness and Browser Compability Testing

## Performance Testing

## Acessibility Testing

Accessibility test carried out using the [Wave Tool](https://wave.webaim.org/)

## User Story Testing

## Manual Testing
