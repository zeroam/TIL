import React, { Component } from 'react'
import TodoItem from '../TodoItem'

class TodoList extends Component {
  shouldComponentUpdate(nextProps, nextState) {
    return this.props.todos !== nextProps.todos;
  }

  render() {
    const { todos, onToggle, onRemove } = this.props
    const todoList = todos.map(
      (todo, i) => (
        <TodoItem
          key={todo.get('id')}
          done={todo.get('done')}
          onToggle={() => onToggle(i)}
          onRemove={() => onRemove(i)}>
          {todo.get('text')}
        </TodoItem>
      )
    )

    return (
      <div>
        {todoList}
      </div>
    )
  }
}

export default TodoList