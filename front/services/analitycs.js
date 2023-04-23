import { get, post } from './service';

export const createReport = (data) => {
    return post(`/analitycs/reports/`, data);
}

export const getReports = () => {
    return get(`/analitycs/reports/`);
}

export const getReport = (slug) => {
    return get(`/analitycs/reports/${slug}/`);
}