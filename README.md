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

### Features Left to Implement

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
