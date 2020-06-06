import React, { Component } from 'react'
import TodoInput from '../components/TodoInput'

import { connect } from 'react-redux'
import { bindActionCreators } from 'redux'

// 액션 생성함수 불러오기
import * as inputActions from '../modules/input'
import * as todoActions from '../modules/todos'

class TodoInputContainer extends Component {
  id = 1
  getId = () => {
    return ++this.id
  }

  handleChange = (e) => {
    const { value } = e.target
    const { InputActions } = this.props
    InputActions.setInput(value)
  }

  handleInsert = () => {
    const { InputActions, TodoActions, value } = this.props
    const todo = {
      id: this.getId(),
      text: value,
      done: false
    }
    TodoActions.insert(todo)
    InputActions.setInput('')
  }

  render() {
    const { value } = this.props
    const { handleChange, handleInsert } = this
    return (
      <TodoInput
        onChange={handleChange}
        onInsert={handleInsert}
        value={value}
      />
    )
  }
}

export default connect(
  (state) => ({
    value: state.input.get('value')
  }),
  (dispatch) => ({
    InputActions: bindActionCreators(inputActions, dispatch),
    TodoActions: bindActionCreators(todoActions, dispatch)
  })
)(TodoInputContainer)