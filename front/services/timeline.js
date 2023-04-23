import { get, post } from './service';

export const getTimeline = () => {
    return get(`/user/timeline/`);
};
