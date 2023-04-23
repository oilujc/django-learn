import React, { useEffect, useState } from 'react';

import Select from 'react-select/async';
import { createInterest, getInterest } from '../../services/interest';

function SetInterests() {

    const [interests, setInterests] = useState([]);
    const [errors, setErrors] = useState([]);

    const promiseOptions = (inputValue) => {
        return new Promise(resolve => {

            if (inputValue.length < 3) {
                resolve([]);
                return;
            }

            getInterest(inputValue).then((res) => {
                const options = res.map((item) => {
                    return {
                        value: item.id,
                        label: item.interest
                    };
                });
                resolve(options);
            });
        });
    }
 

    const handleSelect = (newValue) => {

        if (interests > 6) {
            setErrors(['Solo puedes seleccionar 8 intereses']);
            return;
        }

        console.log('handleSelect', newValue);

        setInterests(newValue);
    }

    const handleSubmit = (e) => {
        e.preventDefault();

        console.log('handleSubmit', interests);

        if (interests.length < 1) {
            setErrors(['Debes seleccionar al menos 1 interes']);
            return;
        }


        if (interests.length > 8) {
            setErrors(['Solo puedes seleccionar 8 intereses']);   
            return;
        }
        

        setErrors([]);


        const data = interests.map((item) => {
            return item.value;
        });
        
        console.log('data', data);


        createInterest(data).then((res) => {
            console.log('createInterest', res);

            window.location.href = '/learning/learn/';
        });

    }





    return (
        <div className="flex flex-col items-center justify-center w-full h-full">
            <h2 className="text-center text-2xl font-bold text-gray-600"
            >¿Cuales son tus intereses?</h2>

            <div className="mt-4 w-full">
                <Select
                    closeMenuOnSelect={false}
                    isMulti
                    placeholder="Selecciona tus intereses"
                    defaultOptions
                    onChange={handleSelect}
                    loadOptions={promiseOptions}
                    value={interests}
                    styles={{
                        control: (base, state) => ({
                            ...base,
                            border: state.isFocused ? '1px solid #c2410c' : '1px solid #f97316',
                            color: '#111827',
                            boxShadow: state.isFocused ? null : null,
                        }),
                        option: (base, state) => ({
                            ...base,
                            backgroundColor: state.isFocused ? '#e2e8f0' : null,
                            color: state.isFocused ? '#1a202c' : null,
                        }),
                    }}

                />
            </div>

            {errors.length > 0 ? (
                <div className="mt-4 w-full">
                    <ul className="text-sm text-red-500">
                        {
                            errors.map((error, index) => (
                                <li key={index}>{error}</li>
                            ))
                        }
                    </ul>
                </div>
            ) : undefined}

            <div className="w-full mt-12">
                <button href=""
                    onClick={handleSubmit}
                    className='inline-flex items-center justify-center w-full px-4 py-2 text-sm font-medium text-white bg-orange-500 border border-transparent rounded-md hover:bg-orange-600 focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-orange-500'
                >
                    Continuar <span aria-hidden="true">&rarr;</span>
                </button>
            </div>
        </div>
    );
}

export default SetInterests;