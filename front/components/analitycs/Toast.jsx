import React, { useState, useEffect } from 'react';


function Toast({ msg, isOpen, onClose }) {

    const [animationClass, setAnimationClass] = useState('opacity-0');

    useEffect(() => {
        if (isOpen) {

            setAnimationClass('slide-in-blurred-bottom');


            setTimeout(() => {                
                handleOnClose();
            }, 5000);
        }
    }, [isOpen]);

    const handleOnClose = () => {
        setAnimationClass('slide-out-blurred-bottom');

        setTimeout(() => {
            onClose();
        }, 500);
    }

    return ( 
        <div className={`fixed bottom-10 right-10 bg-white p-3 z-10 rounded shadow-lg border border-green-300 mt-2 w-96 ${animationClass}`}>
            <div className="flex justify-between">
                <div className='flex flex-col' >
                    <h2 className="text-md font-bold text-gray-600">
                        {msg}
                    </h2>
                </div> 
            </div> 
        </div> 
    );
}

export default Toast;