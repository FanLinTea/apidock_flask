import request from '@/request'

export function gettest(data) {
    return request({
        url: 'config/getcityinfo',
        method: 'post',
        data
    })
}
