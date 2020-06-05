import React, {useState } from 'react'

const EventPractice = () => {
    const [message, setMessage] = useState()
    const [username, setUsername] = useState()

    const handleChange = (e) => {
        if (e.target.name === "username") {
            setUsername(e.target.value)
        } else if (e.target.name === "message") {
            setMessage(e.target.value)
        }
    }

    const handleClick = () => {
        alert(`${username} : ${message}`)
        setUsername('')
        setMessage('')
    }

    const handleKeyPress = (e) => {
        if (e.key === 'Enter') {
            handleClick();
        }
    }

    return (
        <>
            <h1>이벤트 연습</h1>
            <input
                type="text"
                name="username"
                placeholder="유저명"
                value={username}
                onChange={handleChange}
            />
            <input
                type="text"
                name="message"
                placeholder="아무거나 입력해보세요"
                value={message}
                onChange={handleChange}
                onKeyPress={handleKeyPress}
            />
            <button onClick={handleClick}>확인</button>
        </>
    )
}

export default EventPractice