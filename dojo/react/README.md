# ReactJS Dojo


### Challenge
In this challenge, you are asked to add a few features to an existing TODO application. by the end of this session, we wish to have a TODO application with the following features:
* a login/ sign up screen (already implemented)
* display board where TODOs are displayed by their names and grouped by their statuses (already implemented)
* ability to add a TODO (needs to be implemented)
* ability to update a TODO (needs to be implemented)

### Architecture
![Untitled Diagram.png](https://www.dropbox.com/s/7zhdudvt3bhyg3d/Untitled%20Diagram.png?dl=0&raw=1)

### Getting Started
#### Installation and Set Up

Install the dependencies and run the app
```sh
$ git clone https://github.com/slalomdojo/react-dojo.git
$ cd react-dojo
$ docker build -t react-dojo .

For Linux/Mac users:
$ docker run -it -v $PWD:/code -p 8080:8080 -p 7777:7777 react-dojo

For Windows users:
$ docker run -it -v <full path of the current folder>:/code -p 8080:8080 -p 7777:7777 react-dojo

Once you are inside the container:
$ npm run start-dev
```
After running start-dev, you should see the following:
```sh
[1] i wdm : Compiled successfully
```
Navigate to localhost://8080 on chrome and you can see the app running

### Solving the challenge Step by Step
Since this might be the first time you are working with React, we decided to provide some help. 

#### Feature #1 (ability to add a Todo)
We would like to take our simple TODO application to the next level by allowing users to add a Todo Item! Currently , when users click on "Add a Todo" button on the main page, they are taken to an empty page. Your job is to add a simple form on this page that would allow users to submit a Todo.
Here is an example of the end state we are looking for. 
![Screen Shot 2019-04-14 at 9.03.49 PM.png](https://www.dropbox.com/s/amuui0zibv2pvsb/Screen%20Shot%202019-04-14%20at%209.03.49%20PM.png?dl=0&raw=1)
Of course, you can explore your creativity with css and design this form however you wish. 
Here is a Step by Step guide on how to implement this feature:
##### Step 0 (JSX and Expressions)
You might wonder. what is JSX? Short Answer, It's a syntax extension to javascript like HTML.
Expressions can be used in JSX by escaping using curly braces
```js
const element = <h1>Hello, world!</h1>;
return (
  <div> {element} </div>
)
```
[Learn More on JSX](https://reactjs.org/docs/introducing-jsx.html)
##### Exercise:
* Navigate to "TodoForm.jsx". The goal is to add a title to the form we are going to create.
* Add a JSX element to the render method 
* Use expressions to reference the JSX element you created above 
* You can style the title by adding a css rule to App.scss

##### Step 1 (Functional Components, Stateful Components and constructor)
Components let you split the UI into independent, reusable pieces, and think about each piece in isolation. There are two types of components in React:
##### Functional Components: 
* As hinted by the name, these are merely functions.
* They are stateless
* No lifecycle methods
* Accepts a single argument which represents props and returns a React element
* Navigate to "TodoList.jsx". Here we have two functional components: TodoItem and TodoList
##### Stateful Components: 
* Extends React.Component
* Exposes lifecycle methods
* Can contain state
* Stateful components can have a constructor method. you can perform any sort of set up required for your component such as debouncing or binding a method in the constructor. 
* Constructor is called with the initial props of the component.
* In order to use props later in the constructor, Those props must be passed into a call to super. If props is not required, you may omit it.
* Super is required in order to use "this" later in the component

[Learn More on Components](https://reactjs.org/docs/components-and-props.html)
##### Exercise:
* Navigate to "TodoForm.jsx"
* Add a constructor method to this component
* call super inside your constructor
* define the server api url which is `http://localhost:7777`

##### Step 2 (Props and State)
React components store external data using props and internal data in state. Components should behave as pure functions of props and state.
##### Props:
* Props are inputs to pass data into components.
* They are provided by parent components.
* When new props are received, this (usually) triggers the component to re-render.
* Props are read-only. A component should not modify its own props.
##### State:
* Class-based components can store an internal state object.
* Changes in state will (usually) cause the component to re-render (almost) immediately.
* Cannot be used with components defined as functions (aka stateless components).
##### setState
* This function takes either an object of the new state or a function that returns the new state.
* Partial state changes will be shallow-merged with existing state.
* React may batch several calls to setState and apply them simultaneously for performance reasons.
* An optional callback function can be called when the state has finished updating.
##### Exercise:
* Navigate to "TodoForm.jsx"
* Define an initial State inside the constructor - You are going to add attributes to this State object as you build the form in later Steps

##### Step 3 (Uncontrolled Forms)
##### Uncontrolled Forms
* Essentially a basic HTML form
* Use the DOM to access the form values and manage submission
* Typically accessed with a ref prop
* Best when integrating with an existing codebase.

[Learn More on Components](https://reactjs.org/docs/forms.html)
##### Exercise:
* Add a form to the "TodoForm" component
* Add a few elements to the form such as labels and input for Name, Description and a select element to have a drop down for the Status field
* Add a submit button to the form

#####  Step 4 (Controlled Forms)
Any input form element whose value is controlled by React is called a controlled component
* Use component State as the "single source of truth"
* No need for accessing the DOM to get input values
* More performant and flexible than uncontrolled forms

##### Excersice:
* use the state you already added to the "TodoForm" component to hold the values of the form
* Implement handleChange method to bind the form values to the state object
* Implement handleSubmit method to output the state
* set a breakpoint inside the handleSubmit method to ensure we are getting the right values of the form

##### Step 5 (Http requests using Axios)
* Axios is a lightweight HTTP client based similar to a Fetch API
* Axios is promise-based async/await library for the readable asynchronous code
##### Exercise:
* construct a new TODO object using the values the state is holding
* Use axios to to submit a POST call to the following endpoint:http://localhost:7777/task/new
* append the new TODO object in the body of this request call
* the TODO Object should have the following attributes:
    - name
    - status
    - description
    - ETA
* Upon successful completion of this step, You should get a 200 response back from the API
* Once you got "success", Navigate back to the form and ensure the new TODO is added to the Board

#####  Step 6 (Routing)
* One way to redirect users to a new location is to use the Redirect Component
* Redirect component accepts a "to" parameter which can be the name of the new path

##### Exercise:
* redirect users to the main page after the submit call is successful
* notice Redirect is imported from "react-router" library

## Feature #2 (ability to update a Todo)
Now that we can add a Todo, we would like to let users update a Todo. Your job is to navigate users to a new page upon clicking on the title of a Todo on the main display board. This is the end state we are looking for:

![Screen Shot 2019-04-16 at 9.48.17 AM.png](https://www.dropbox.com/s/7m9u0m9xzfb4e14/Screen%20Shot%202019-04-16%20at%209.48.17%20AM.png?dl=0&raw=1)

Here is a step by step guide on how to achieve this:

##### Step 0 (Navigation)
* In TodoItem component, examine how the Navigation is enabled using Link from 'react-router-dom'
* Examine the 'todoDetail' object in the same component. Notice the pathname for the new page and the fact that we are passing the todo object using Link 
* Navigate to UpdateTodo component. Here , we would like to use the same TodoForm to achieve code reusability. render a "TodoForm" component.

##### Step 1 (Passing Props to the TodoForm component)
* In the UpdateTodo component, pass the todo object to the form
* In the TodoForm component, if a todo object is passed to this component, Update the state to hold the values for status, description, ETA and Name of the todo

##### Step 2 (Http Call for Updating the Todo)
* Upon submit, check to see if this is an update or add request
* If it is an update request, retrieve the values of the form from the state
* Use axios to to submit a POST call to the following endpoint:http://localhost:7777/task/update and append the updated todo
* check the network tab to ensure you get a successful response
* Notice, that if you refresh the page, all the values for the form are lost. brainstorm possible ways to solve this




