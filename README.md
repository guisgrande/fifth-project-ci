# Street Craft - Store

Street Craft is an online store selling skateboards and other products using graffiti street art as design. A B2C business with a vision to reach their target audience (people interested in skateboarding and street style) through the internet. With the mission to deliver quality products through a reliable, fast and intuitive online sales platform. 

## Contents

## UX/UI Design

During the elaboration of the project, the aspects for the final result to respect a good UX (User experience) and UI (User interface) behavior were taken into consideration, thus delivering a quality project where the user can follow the steps of a purchase without difficulties or complications.

### Strategy

#### Site owner goals

As mentioned, the project is an e-commerce project. I chose as the main product to be commercialized in the online store the skateboard with the theme of using real street art (graffiti) as design. To complement the product options were also added hats and bags. The business model is B2C where our target audience are direct consumers.

The idea for marketing and promotion would be the presence in social networks targeting the topics of skateboarding, graffiti, hip hop / rap community and other street sports. With a well designed SEO for the website and that transmits confidence and transparency to users, I believe it would be a project with potential for success.

  - The Street Craft e-commerce store aims to be responsive on multiple devices to reach and be available to as many people as possible.
  - Be practical to register and access the account/profile for users who wish to do so.
  - So that users can easily add products to their bag and also modify it with convenience.
  - That users can view offers and discounted prices.
  - That the online store has a practical and simple checkout, requesting only the most important information to finish the order safely.
  - That the website provides feedback on important user actions, such as messages informing when logged in, logged out, when the order was completed, or at other relevant times.
  - That users can review their information when necessary, like delivery details, order details or status.

#### Agile

For the development of this project, the Agile methodology was applied. As a support tool, I used the GitHub projects.

- To visualize the project access this link > [Agile Street Craft](https://github.com/users/guisgrande/projects/2)

As you can see, we used a simple Kanban board with the fields (To do, Doing, Done). To do the next ones that will be executed, Doing the ones that are currently being developed and Done the ones that were finished.

The final structure after the elaboration was 6 different epics and a total of 32 User Stories distributed among them. In the following image, I detail the EPICs and their respective US.

<details>
    <summary>Agile Structure</summary>
    <div align="center">
      IMAGE HERE
    </div>
</details> 

To run agile most efficiently, the following Sprints were determined as per the following image. The User Stories __#18 Filter products__  was not implemented in the project at this moment, being on stand by for future updates.

<details>
    <summary>Agile Sprints</summary>
    <div align="center">
      IMAGE HERE
    </div>
</details>

#### User stories

- As an user, I want to know what kind of products I will find in the store, so I can decide if it is the product of my interest.
- As an user, I want to see which products are on sale, so I can add them to my bag if the price attracts me.
- As an user, I want to easily add or remove products from my bag, so I can adapt my product selection according to my needs.
- As an user, I want to easily proceed to the checkout when I finalize my choice, so I can complete the purchase without complications.
- As an user, I want to see that my order has been successfully completed, so I can be sure that the payment proceeded correctly.
- As an user, I want to register or connect with the company, so I can be informed with the news and promotions.
- As a site owner, I want to easily add, edit or remove products, so I can provide new products or correct some information.
- As a site owner, I want to send a communication to the subscribers of the site, so I can send promotions and communications.
- As a site owner, I I want to update stock and order status, so I can keep accurate information.

### Scope

For the scope of this project the following key points were determined.
- Create a webpage application using the Django framework.
- Create a checkout using Stripe as payment method tool.
- Use bootstrap to make the site responsive, and custom CSS and Java Script to complement.
- The website should be functional and intuitive, easy to navigate and proceed to checkout.
- Allow the user to create an account to keep the information saved.
- Allow users to manipulate their delivery details informations.
- Allow the user to add and manipulate the products in the bag before checkout.
- Allow the site owner add, update or remove produtos direct from the website.
- Allow the site owner to update stock and order status direct from the website.

### Structure

The page structure for Street Craft Store was determined as follows:
- Home, profile, products (filter pages for: Categories / Offers), shopbag, checkout (checkout page / checkout success), management (Product Manag. / Stock Manag. / Order Status Manag. / New Letter Manag.).

For __users not logged in__, will be displayed:
- Home, products (filter pages for: Categories / Offers), sign in, sign up, shopbag, checkout (checkout page / checkout success).

For __users logged in__, will be displayed:
- Home, products, My account (My profile / Logout), shopbag, checkout (checkout page / checkout success).
- My profile will contain My orders, Change password, Coupon info, Delete profile and Update delivery information.

For __superuser (site owner) logged in__, will be displayed:
- Home, products (filter pages for: Categories / Offers), management (Product Manag. / Stock Manag. / Order Status Manag. / New Letter Manag.), My account (My profile / Logout), shopbag, checkout (checkout page / checkout success).
- My profile will be the same as users.

### Skeleton

#### Wireframes

The wireframe was created using the Figma tool. During the elaboration of the wireframes, I added what the front end should look like. At the end of the development some changes were made.

- To visualize full desktop wireframe project > [Figma - Street Craft Desktop](https://www.figma.com/file/cNH4NoT9CU6UJT8fp4qUqO/PP5?node-id=4%3A187&t=37SdRfbrboNm8mZH-0)

<details>
    <summary>Wireframes - Desktop</summary>
    <div align="center">
      IMAGES HERE
    </div>
</details>

- To visualize full mobile wireframe project > [Figma - Street Craft Mobile](https://www.figma.com/file/cNH4NoT9CU6UJT8fp4qUqO/PP5?node-id=0%3A1&t=37SdRfbrboNm8mZH-0)

<details>
    <summary>Wireframes - Mobile</summary>
    <div align="center">
      IMAGES HERE
    </div>
</details>

#### Database diagram

The database for Street Craft was designed to determine all the models present in the project and their relationships.

Regarding the purchase and checkout process, the user may or may not be logged in. It is possible to finish the purchase without an account. The selected products are added to the shopbag and when accessing the checkout, the information is automatically transferred.

Regarding the coupon only logged in users have access to it.

<details>
    <summary>Diagram</summary>
    <div align="center">
      IMAGE HERE
    </div>
</details>

### Surface

#### Colour scheme

For the Street Craft project I used predominantly standard Bootstrap colors.

The custom colors I determined to use were as follows. These are applied to the navigation bar and footer. 

For the texts, the colors white or black were applied according to the background color to have the proper contrast.

<details>
    <summary>Colour scheme</summary>
    <div align="center">
        IMAGE HERE
    </div>
</details>

#### Typography

The site's font was chosen from google fonts. I chose the Syne Mono (REgular 400) font. It was used throughout the entire site, including titles and body.

#### Imagery

To increase the visual response of the e-commerce I selected some images related to the products/theme of the project. The images for the website were acquired from Unsplash and the ones used for the products were from Canva.

On the home page I used three cartoon images as the hero section.

Another image was used as background for the accounts pages/templates.

Bootstrap icons were used to give more emphasis to the titles.

## Features

### Existing Features

#### __Favicon__

- Favicon is loaded on every page, the little logo is also present in the navbar.

<div align="center">
    IMAGE HERE
</div>

#### __Navbar__

- Navbar that is present on all pages for user navigation through the online store. 
- Is present for everyone the logo/banner that redirects to the home page, the search bar, a link to Home, a link to Shop(Dropdown) - All Products / Select Category(Skateboards / Caps & Hats / Backpacks & Bags) / Special Offers(New Arrivals / Special Sale / Las Chance), a shopbag where display Bag icon, total of products and value.

- The other links are displayed depending on whether the user is logged off or not, and what type of account.

- For not logged users, the links are displayed: : Sign in and Sign up.

<div align="center">
    IMAGE HERE
</div>

- For logged users, the links are displayed: : My Account(Dropdown) - My Profile / Logout

<div align="center">
    IMAGE HERE
</div>

- For logged superusers, the links are displayed: : My Account(Dropdown) - My Profile / Logout and Management(Dropdown) - Product Manag. / Stock Manag. / Order Status Manag. / News Letter Manag.

<div align="center">
    IMAGE HERE
</div>

- Navbar is responsive, for mobiles it automatically groups to drowdown menu.

<div align="center">
    IMAGE HERE
</div>

#### __Footer__

- The footer is shown only when reaching the end of the page, it counts with a few navegation links, News Letter - Subscribe button and Social links.

- For not logged users, the links are displayed: : Home / All Products / Sign in / Sign up.

<div align="center">
    IMAGE HERE
</div>

- For logged users and superusers, the links are displayed: : Home / All Products / My Profile / Logout.

<div align="center">
    IMAGE HERE
</div>

- The News Letter - Subscribe button, open a modal form when clicked. Where the user can subscribe using e-mail and a name.

<div align="center">
    IMAGE HERE
</div>

- The Social links are four in total, they open a new page of the corresponding social network when clicked.

<div align="center">
    IMAGE HERE
</div>

#### __Home Page - Hero__

At the beginning of the home page, the first section has a carousel of images, three in total. Each one counts with a call text and a button that redirects to a different page of the site.

- First slide: The button redirects to the products page
- Second slide: The button redirects to registration page
- Third slide: The button redirects to skateboards page only.

<div align="center">
    IMAGE HERE
</div>

#### __Home Page - New Arrivals__

- The New Arrivals section has custom text to call the user into action and the SHOP button when clicked redirects the user to a page with the products in that specific offer. On the initial page, only the last four products of this promotion are displayed, and it is possible for the user to add the product to the shopbag already from that moment on.

<div align="center">
    IMAGE HERE
</div>

#### __Home Page - Special Offers__

- The Special Offers section has custom text to call the user into action and the SHOP button when clicked redirects the user to a page with the products in that specific offer. On the initial page, only the last four products of this promotion are displayed, and it is possible for the user to add the product to the shopbag already from that moment on.

<div align="center">
    IMAGE HERE
</div>

#### __Home Page - Last Chance__

- The Last Chance section has custom text to call the user into action and the SHOP button when clicked redirects the user to a page with the products in that specific offer. On the initial page, only the last four products of this promotion are displayed, and it is possible for the user to add the product to the shopbag already from that moment on.

<div align="center">
    IMAGE HERE
</div>

#### __Home Page - News Letter__

- This section has text to attract the user's attention to register to the News Letter, and has required fields for e-mail and name, and a subscribe button.
- Upon registration the user receives an e-mail confirming registration and a message is also reflected on the website.

<div align="center">
    IMAGE HERE
</div>

#### __Home Page - Social__

- This section also has a text to attract the user to follow Street Craft pages on social networks
- The Social buttons are four in total, they open a new page of the corresponding social network when clicked

<div align="center">
    IMAGE HERE
</div>

#### __Home Page - Sign up Coupon__

- The last section of the home page is visible only to users logged in. It contains a text explaining and inviting the user to create an account for a 10% discount coupon.
- The button redirects the user to the registration page.

<div align="center">
    IMAGE HERE
</div>

#### __Sign up__

- Registration page, with a simple form with the field for username, e-mail twice and for password twice, a button to register. A short text that calls who already has a registration to the login page.

<div align="center">
    IMAGE HERE
</div>

#### __Sign in__

- Access page, with two fields to be filled in (username/e-mail and password) or login using Google account. 
- A button to log in and another to forgot password. A remember me check is also present.
- A short text with a callout for those who don't have an account.

<div align="center">
    IMAGE HERE
</div>

#### __Sign out__

- Page for logged in users who have selected the logout option, it asks if they really want to perform this action.

<div align="center">
    IMAGE HERE
</div>

#### __Forgot Password__

- Page for the user to recover the password, there is a text with the necessary action, a field for the e-mail and a button to reset the password. 
- By clicking the button an e-mail is sent with a new link to change the password.

<div align="center">
    IMAGE HERE
</div>

#### __My Profile__

- Returns the username from which account you are logged in.
- It shows some account options like: a button for My Orders, a field to show active coupons, a button to change the password and another button to delete the profile.
- The delivery data is available as a form that can be changed. By clicking the update info button the information entered into the fields is saved and a success message is displayed

<div align="center">
    IMAGE HERE
</div>

#### __My Orders__

- Returns the total orders of the logged in user.
- A list with the following information: Order Number / Date / Items / Order Total 
- The Order Number ia a link to redirect to that order details page.

<div align="center">
    IMAGE HERE
</div>

#### __Order Details__

- It shows the details of the order. It is possible to see the order number, date, products and quantity, billing info, delivering info, contact info and order status.
- The Order Status returns what step the order is currently at, and the next and completed steps
- It also has two buttons, one to go back to My Profile page and the other to My Orders.

<div align="center">
    IMAGE HERE
</div>

#### __Change Password__

- Hhave three fields to fill in on the form. The first is the current password and the other two are for the new password. I only need the second to secure and confirm the new password. 
- It also has two buttons, one Change Password and Back to My Profile.

<div align="center">
    IMAGE HERE
</div>

#### __Delete Profile__

- Area for the user to confirm that he really wants to delete the account. Rephrase the question informing that all data will be deleted when confirming. 
- If the user has any active orders in the system, a warning is loaded on the page so that he can write down the necessary information. And a button to redirect to My Orders.
- A button to cancel (redirect to My Profiel) and a link back to shop.

<div align="center">
    IMAGE HERE
</div>

#### __All Products__

- The main page for displaying the store's products. 
- At the top, it shows how many products there are for a given search / filter. A selection box is present to sort among all products, sorted by price or name.
- It has 8 products per page.
- The user can add the product to the shopbag via the product card container and select the quantity.
- By clicking on the product image, the user is redirected to the product detail page.
- By selecting the category or offer in the navigation bar the user will only see the products in that specific filter.

<div align="center">
    IMAGE HERE
</div>

#### __Product Details__

- It shows a picture of the product and just below the average reviews. If the user is logged in, a button is displayed that redirects to the reviews page.
- It is possible to see all information, name, SKU, offer if any, price (discounted price if any), description.
- Quantity field (Less / More buttons).
- Buttons for KEEP SHOPPING (back to products page) and ADD TO BAG.
- If logged as superuser the buttons to edit and delete product are visible at the end.
- Delete product button, redirect to a new page to confirm action.

<div align="center">
    IMAGE HERE
</div>

#### __Shopbag__

- If the shopbag is empty, only a text is displayed and the button to KEEP SHOPPING
- It shows a list with the added products.
- A product image with the name, sku and unit price.
- A field to modify the quantity with the button to update. And the button to remove the product.
- The order and delivery totals are displayed.
- If the user is logged in, a field to add the discount coupon is displayed and the button to apply it. If it is valid the discount is applied and the discount field is displayed.
- At the end are the buttons for KEEP SHOPPING (back to products page) and SECURE CHECKOUT (redirect to checkout page).

<div align="center">
    IMAGE HERE
</div>

#### __Checkout__

- It shows a Order Summary with a resume of the order.
- A form with contact and delivery information to be filled in. If the user is logged in and has the information saved, these fields are automatically filled in.
- If user not logged display option links to create an account ou to login. If user are logged in, display a check bos to auto save the form information to profile.
- Field for credit card data, using the Stripe tool.
- At the end are the buttons for Adjust Bag (back to shopbag page) and Complete Order (submit the form if valid, and redirect to success checkout page).

<div align="center">
    IMAGE HERE
</div>

#### __Checkout Success__

- As soon as the order is processed and payment has been confirmed successful, an e-mail is sent to the user with the order information and the order number.
- It shows the details of the order. It is possible to see the order number, date, products and quantity, billing info, delivering info, contact info.
- At the end have one button Check out the latest promotions (redirect to products page)

<div align="center">
    IMAGE HERE
</div>

#### __Managemente - Add Product__

- Accessible only to superuser. 
- It has a form for the site owner to easily add new products to the store.
- One button for cancel(redirect to My Prodile page) and one button for add product (If valid, submit form and add new product).
- When added a success message appears

<div align="center">
    IMAGE HERE
</div>

#### __Managemente - Stock__

- Accessible only to superuser. 
- Shows a list of all products on the site. A column with the information name/ku, current stock and update stock.
- Each product has a line, where site owner can enter the quantity to be updated and confirm with the check `✓` button.
- When updated a success message appears

<div align="center">
    IMAGE HERE
</div>

#### __Managemente - Order Status__

- Accessible only to superuser. 
- Shows a list of all orders on the site. A column with the information order number, date, current status and update status.
- Each order has a line, where site owner can select the status to be updated and confirm with the check `✓` button.
- When updated a success message appears

<div align="center">
    IMAGE HERE
</div>

#### __Managemente - News Letter__

- Accessible only to superuser. 
- Shows the total number of registered e-mails, a field to enter the subject and another to enter the message (body). 
- The button to send the e-mail to everyone.
- When sent a success message appears

<div align="center">
    IMAGE HERE
</div>

#### __Marketing - Custom Facebook Page__

- A customized page for the store was created on Facebook. In order to increase the presence of the store on social networks. 

<div align="center">
    IMAGE HERE
</div>

### Features Left to Implement

- For the future implement the User Stories __#18 Filter products__ that has not been completed at this time. To allow users to better filter the results.
- Create a section where the user can customize his skateboard.
- Allow users to comment along with their reviews.
- Add another model for coupons that can be used by anyone, to be used in a promotional campaign.

## Testing

### Fixed Bugs

### Unfixed Bugs 

## Deployment

### Deployment

### Fork

### Clone

## Technologies and tools

- Programming languages used: Python 3.8, Java Script, HTML5 and CSS3.

- [Gitpod](https://www.gitpod.io/) - Used to create/edit the code of the project.
- [Github](https://github.com/) - Used to create repository, for version control and Agile project.
- [Heroku](https://heroku.com/) -  Used to deploy the project.

## Credits

### Code

### Content

### Media

## Acknowledgements

- Code Institute for all the support and the team always ready to help.
- My mentor [Ben Kavanagh](https://github.com/BAK2K3) for all the instructions, advice and knowledge that helped me to improve the project.
- My parents, my wife and my friends for motivating me to achieve my best.
- Everyone in the Slack community for tips and opinions. 
