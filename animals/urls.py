from django.conf.urls import url
from django.urls import path
from .views import index, gallery, blog, contacts_us, view_single, view_all_posts, add_comment, delete_comment, add_personal_post, add_new_post, view_add_blog, delete_post, update_post_list, update_post_blog, view_single_blog, add_post, adding_post
urlpatterns = [

    url(r'^$', index, name='index'),
    url(r'^gallery$', gallery, name='gallery'),
    url(r'^blog$', blog, name='blog'),
    url(r'^blog-colllection$', view_all_posts,
        name='blog-colllection'),  # all_blog_for_admin
    url(r'^add-personal-post$', add_personal_post, name='add-personal-post'),
    url(r'^contact-us$', contacts_us, name='contact-us'),
    url(r'^view_single/(?P<post_id>\d+)$', view_single,
        name='view-single'),  # palitan ko to for single view
    url(r'^delete_comment/(?P<comment_id>\d+)$',
        delete_comment, name='delete-comment'),
    url(r'^add_comment$', add_comment, name='add-comment'),  # add_comment
    url(r'^adding_post$', adding_post, name='adding_post'),  # add_post
    url(r'^view-add-blog$', view_add_blog, name='view-add-blog'),  # view_post
    url(r'^delete_post/(?P<post_id>\d+)$',
        delete_post, name='delete_post'),  # delete
    url(r'^update_post_list/(?P<post_id>\d+)$', update_post_list,
        name='update_post_list'),  # update_post_view_single
    url(r'^update_post_blog$', update_post_blog,
        name='update_post_blog'),  # update_pos_single
    url(r'^view_single_blog/(?P<post_id>\d+)$', view_single_blog,
        name='view_single_blog'),  # update_status_view_single
    # url(r'^update_status$', update_status, name='update_status')#update_status_single
    url(r'^add_post$', add_post, name='add_post'),  # add_post from
    url(r'^add_new_post$', add_new_post, name='add_new_post'),  # add_ from blog




]
