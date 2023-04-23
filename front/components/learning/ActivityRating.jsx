import React, { useState } from 'react';
import Activity from './Activity';

import Swal from 'sweetalert2'
import { useForm, Controller } from 'react-hook-form';
import { createuserActivityRating } from '../../services/learning';



function ActivityRating({ activity }) {

    const { control, getValues, watch, handleSubmit, formState: { errors } } = useForm({
        defaultValues: {
            rating: 0,
        }
    });

    const [responseErrors, setResponseErrors] = useState(null);

    const onSubmit = (data) => {
        createuserActivityRating({
            activity: activity.id,
            rating: data.rating,
        }).then((response) => {

            if (!response.id) {
                setResponseErrors(response);
                return;
            }

            setResponseErrors(null);

            Swal.fire({
                title: 'Gracias por tu opinión',
                text: 'Tu opinión nos ayuda a mejorar',
                icon: 'success',
                confirmButtonText: 'Continuar',
            }).then((result) => {
                if (result.isConfirmed) {
                    window.location.href = '/feed/';
                }
            });
        });

    }


    return (
        <div className="flex flex-col mb-2">
            <div className="rounded shadow-lg p-3 border border-gray-300">
                <div className="flex flex-col mb-2">
                    <h2 className="text-sm text-gray-600">
                        Ayudanos a mejorar
                    </h2>
                    <p className="text-xl font-bold text-gray-700">
                        ¿Qué te pareció esta actividad?
                    </p>
                </div>

                <div className="mt-4 mb-5 text-gray-600">
                    <Controller
                        control={control}
                        name="rating"
                        rules={{ required: true }}
                        render={({ field }) => (
                            <div className="flex justify-between">
                                <div className="flex flex-col items-center">
                                    <input type="radio" {...field} value="1" />
                                    <label className="ml-2">Muy mala</label>
                                </div>
                                <div className="flex flex-col items-center">
                                    <input type="radio" {...field} value="2" />
                                    <label className="ml-2">Mala</label>
                                </div>
                                <div className="flex flex-col items-center">
                                    <input type="radio" {...field} value="3" />
                                    <label className="ml-2">Regular</label>
                                </div>
                                <div className="flex flex-col items-center">
                                    <input type="radio" {...field} value="4" />
                                    <label className="ml-2">Buena</label>
                                </div>
                                <div className="flex flex-col items-center">
                                    <input type="radio" {...field} value="5" />
                                    <label className="ml-2">Muy buena</label>
                                </div>
                            </div>
                        )}
                    />

                    {
                        errors.rating && (
                            <div className="text-red-500 text-sm">
                                {errors.rating}
                            </div>
                        )
                    }

                    {
                        (responseErrors && responseErrors['rating']) && (
                            <div className="text-red-500 text-sm">
                                {responseErrors['rating']}
                            </div>
                        )
                    }

                <Activity activity_id={activity.slug} classNames={'p-3'} wFav={false} />
            </div>

            <div className="flex justify-end w-100">
                <button className="bg-orange-500 text-white p-2 rounded text-center block" onClick={handleSubmit(onSubmit)}>
                    Finalizar
                </button>
            </div>
        </div>
        </div >
    );
}

export default ActivityRating;