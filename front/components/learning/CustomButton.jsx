import React, { useState } from 'react';

function CustomButton({ onClick, children, backgroundColor = 'bg-gray-200', textColor = 'text-gray-700', wFade = false, args = null}) {

    const [animationClass, setAnimationClass] = useState('');

    const clickHandler = () => {
        if (wFade) {
            setAnimationClass('fade-out');
        }

        setTimeout(() => {

            if (args) {
                onClick(args);
            } else {
                onClick();
            }
        }, 100);
    }

    return (
        <button className={`p-2 rounded text-center block ${backgroundColor} ${textColor} ${animationClass}`} onClick={clickHandler}>
            {
                children
            }
        </button>
    );
}

export default CustomButton;