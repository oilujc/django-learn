import React, { useState, useEffect } from 'react';
import { useForm, Controller } from 'react-hook-form';

import Select from 'react-select';
import CustomButton from './CustomButton';

function WordReinforcement({ activity, onClick, isOpen }) {

    const { control, getValues, watch, handleSubmit, formState: { errors } } = useForm({
        defaultValues: {
            words: [],
        }
    });

    const [animationClass, setAnimationClass] = useState('opacity-0');


    useEffect(() => {
        if (isOpen) {
            window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' })

            setTimeout(() => {
                setAnimationClass('swing-in-top-fwd');
            }, 200);
        }
    }, [isOpen]);

    const onSubmit = (data) => {
        console.log(data);
    }

    const handleButton = () => {
        if (activity && activity.lesson_count !== activity.progress_count) {
            onClick();
        }

        return;
    }

    return (
        <div className={"rounded shadow-lg p-3 border border-gray-300 mt-2 " + animationClass}>
            <div className="flex justify-between">
                <div className='flex flex-col' >
                    <h2 className="text-lg font-bold text-gray-600">
                        Tienes problemas con el significado de algunas palabras?
                    </h2>
                </div>
            </div>
            <div className="mt-2 mb-5 text-gray-600">

                <Controller
                    control={control}
                    name="words"
                    render={({ onChange, value, name, ref }) => (
                        <Select
                            options={[]}
                            onChange={onChange}
                            value={value}
                            name={name}
                            inputRef={ref}
                            closeMenuOnSelect={false}
                            isMulti
                            placeholder="Indicanos las palabras que no entiendes"
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
                    )}
                />

            </div>
            {
                <div className="flex justify-between w-100">
                    <CustomButton onClick={handleButton} >
                        Continuar
                    </CustomButton>
                    <CustomButton onClick={handleButton} backgroundColor='bg-orange-500' textColor='text-white' >
                        Guardar y continuar <span aria-hidden="true">&rarr;</span>
                    </CustomButton>
                </div>
            }
        </div>
    );
}

export default WordReinforcement;