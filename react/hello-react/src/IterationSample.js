import React, { useState } from 'react'

const IterationSample = () => {
    const [name, setName] = useState()
    const [names, setNames] = useState(['눈사람', '얼음', '눈', '바람'])

    const handleChange = (e) => {
        setName(e.target.value)
    }

    const handleInsert = () => {
        setNames(names.concat(name))
        setName('')
    }

    const handleRemove = (index) => {
        setNames([
            ...names.slice(0, index),
            ...names.slice(index + 1, names.length)
        ])
    }

    const nameList = names.map(
        (name, index) => (
            <li 
                key={index}
                onDoubleClick={() => handleRemove(index)}>
                {name}
            </li>
        )
    )

    return (
        <div>
            <input
                onChange={handleChange}
                value={name} />
            <button onClick={handleInsert}>추가</button>
            <ul>
                {nameList}
            </ul>
        </div>
    )
}

export default IterationSample