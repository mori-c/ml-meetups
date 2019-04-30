import React from 'react';
import axios from 'axios';
import { Redirect } from 'react-router';
import './App.scss';

const statusEnum = {
  DONE: "Done",
  TODO: "To Do",
  InProgress: "In Progress"
}

export class TodoForm extends React.Component
{

  // react.constructor METHODS {
  // add this.super
  // def super.api( http://localhost:7777)
  // }

  constructor ( props )
  {
    super( props );
    const apiurl = "http://localhost:7777";
    this.state = { value: '' };
    this.handleChange = this.handleChange.bind( this );
    this.handSubmit = this.handleSubmit.bind( this );
  }
  handleChange( event )
  {
    this.setState( { value: event.target.value } );
  }
  handleSubmit( event )
  {
    alert( 'Yo, name was submitted: ' + this.state.value );
    event.preventDefault();
  }
  render()
  {
    const element = <h1> TodoForm</h1>;
    return (
      <div> {element}
        <form onSubmit={this.handleSubit}>
          <label>
            Name:
            <input type="text" name="name" value={this.state.value} onChange={this.handleChange} />
          </label>
          <br />
          Description:
          <input type="text" name="description" />
          <br />
          Select:
          <select name="items">
            <option value="eta1">ETA 1</option>
            <option value="eta2">ETA 2</option>
          </select>
          <br />
          <input type="submit" value="Submit" />
        </form>
      </div>
    );
  }
}


