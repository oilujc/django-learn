import { get, post, destroy } from './service';

export const getLesson = (slug) => {
    return get(`/learning/lesson/${slug}/`);
};

export const createLessonLike = (data) => {
    return post(`/learning/lesson-like/`, data);
}

export const deleteLessonLike = (id) => {
    return destroy(`/learning/lesson-like/${id}/`);
}

export const createActivityProgress = (data) => {
    return post(`/learning/activity-progress/`, data);
}

export const getUserActivities = () => {
    return get(`/learning/user-activity/`);
}

export const createUserActivity = (data) => {
    return post(`/learning/user-activity/`, data);
}

export const getUserActivity = (slug) => {
    return get(`/learning/user-activity/${slug}/`);
}

export const createUserActivityLike = (data) => {
    return post(`/learning/user-activity-like/`, data);
}

export const deleteUserActivityLike = (id) => {
    return destroy(`/learning/user-activity-like/${id}/`);
}

export const createuserActivityRating = (data) => {
    return post(`/learning/user-activity-rating/`, data);
}