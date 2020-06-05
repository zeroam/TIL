import React, { useState, useRef } from 'react'
import './ValidationSample.css'

const ValidationSample = () => {
    const [password, setPassword] = useState('')
    const [clicked, setClicked] = useState(false)
    const [validated, setValidated] = useState(false)

    const input = useRef()

    const handleChange = (e) => {
        setPassword(e.target.value)
    }

    const handleButtonClick = (e) => {
        setClicked(true)
        setValidated(password === '0000')
        input.current.focus()
    }

    return (
        <div>
            <input
                ref={input}
                type="password"
                value={password}
                onChange={handleChange}
                className={clicked ? (validated ? 'success' : 'failure') : ''}
            />
            <button onClick={handleButtonClick}>검증하기</button>
        </div>
    )
}

export default ValidationSample