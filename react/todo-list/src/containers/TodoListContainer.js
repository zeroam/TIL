import React, { Component } from 'react'
import TodoList from '../components/TodoList'

import { connect } from 'react-redux'
import { bindActionCreators } from 'redux'

import * as todoActions from '../modules/todos'

class TodoListContainer extends Component {
  handleToggle = (id) => {
    const { TodoActions } = this.props
    TodoActions.toggle(id)
  }
  
  handleRemove = (id) => {
    const { TodoActions } = this.props
    TodoActions.remove(id)
  }

  render() {
    const { todos } = this.props
    const { handleToggle, handleRemove } = this

    return (
      <TodoList 
        todos={todos}
        onToggle={handleToggle}
        onRemove={handleRemove}
      />
    )
  }
}

export default connect(
  (state) => ({
    todos: state.todos
  }),
  (dispatch) => ({
    TodoActions: bindActionCreators(todoActions, dispatch)
  })
)(TodoListContainer)