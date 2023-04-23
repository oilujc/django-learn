import { get, post } from './service';

export const getInterest = (kw) => {
    return get(`/user/interests/?search=${kw}`);
};

export const createInterest = (data) => {
    return post(`/user/interests/`, {
        interests_ids: data,
    });
}