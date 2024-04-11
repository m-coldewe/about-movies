# about-movies

# Introduction

Movies have the ability to bring people together from diverse cultures and backgrounds. They help translate ideas, concepts, themes, into a format which is easily accessible to all. With about-movies, we seek to create a full-stack application to visualize the dataset using interactive graphs and maps that anyone can use and take meaning from. 

# Tools

For our application, we use Plotly Dash in conjunction with Plotly Express, Dash Bootstrap Components, and Pandas to build out the graphs and interactive elements, and filter the data. 

# Requirements


# Process

### Data Cleaning
The dataset required minnimal cleaning. We removed extraneous commas, changed the budget and gross columns to appropriate numeric types, removed extra spaces, and renamed the Music and romance columns. Then, because we wanted to look at the profit, both worldwide and domestic, we subtracted the respective film budgets from the gross, and ended by reorganizing the columns for better readability. 

Finally, we created the database using splite3.

### Setting up the app
For the application, we chose Plotly Dash because it was more flexible than Flask and more accesible than [not-ninja].

While we had the option to put everything in a single page, we opted to create a multi-page application using Dash's Pages feature, instead. With Pages, we created a container page, app.py, which holds the app initiation and nagivation links, and sets the basic overall layout for the following pages. 

### Home
Our homepage contains our welcome and basic identification information, along with an automatic carosel to display relevant images set up using bootstrap components and Dash's Container system, which uses Rows and Columns for spacing and styling through class names instead of css. 

### About
Our About page also uses bootstrap components and the container system to create distinct blocks of data to hold member information and information about the dataset we used, along with relevant links to better connect the user with additional information.

### Data
The Data page (table.py) pulls the dataset from the sqlite database to display the entire dataset used for this project in a searchable format so that anyone who wants to search the information contained within may. It uses the Dash DataTable with CSS styling to give it the black-red-and-white color scheme.

### Map
The map page, which looks at the productions through the Studios that distributed them, shows the physical location of each stuido along with a selection of interesting information through a hover. It uses plotly express in conjunction with plotly graph objects, and displays neatly using Dash html and Dash Core Components. 

### Financials
For Financials, we look at budget and profit in a pair of bar graphs that visualizes the movement of money for the years from 1977 to 2019. The graphs use plotly express with dash dependencies, and are organized within the page using dash bootstrap components.

### Genres
The genres page looks at the number of movies released, by genre, for each year within the dataset. Due to the way the genre columns were set up, it requires a little addditional manipulation prior to mapping. The graph displays using plotly express, Dash html and Dash Core Components.

### Durations
The film length page looks at the relationship between the length of the film and the MPAA rating it earned to discern if there exists a relationship, postive or negative, between them. The graph uses plotly express and Dash Core Components, and adds callback, Input and Output to deliver interactivity, allowing the user to switch easily between the different MPAA ratings to see the different trends.

### Ratings
The Ratings page looks at the relationship between the rating of each film and the worldwide profit to see if a particular rating tends to enjoy greater profitability. The graph uses plotly express, Dash Core Components, and Dash dependencies, as well as callback, Input, and Output. The combination adds interactivity, allowing the user to view each rating independent and better visualize the relationship.

### Distribution
The Distribution page shows how each movie compared to the other top performing movies for the year it was released, for each of the years within the dataset. The graph uses plotly express with Dash dependencies, Input and Outout, as well as Dash Core components and callback, to deliver different year views within the same graph figure per the user's selection.   
 
# Results

### Home

![image](https://github.com/m-coldewe/about-movies/assets/152930492/7ac19f78-1a48-41bd-b21d-5e4694df0a58)

### About



### Data



### Genres

### Durations

### Ratings

### Distribution

### Financials

### Map

# Summary
Using Plotly Dash, we created
