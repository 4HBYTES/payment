import unittest
import mock
import json

from mock_page_service import MockPageService

import app

# TODO: do not keep this global
mock_page_service = MockPageService()


class BlogTests(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    @mock.patch('app.pages.resources.PageList.service.get_all', side_effect=mock_page_service.get_all)
    def test_get_all_pages(self, mock_get_all):
        rv = self.app.get('/page/')

        self.assertEqual(rv.status_code, 200)
        mock_get_all.assert_called_with()

    @mock.patch('app.pages.resources.PageDetail.service.get_by_slug', side_effect=mock_page_service.get_by_slug)
    def test_get_single_page(self, mock_get_by_slug):
        rv = self.app.get('/page/my-post')

        self.assertEqual(rv.status_code, 200)
        mock_get_by_slug.assert_called_with('my-post')

    @mock.patch('app.pages.resources.PageDetail.service.get_by_slug', side_effect=mock_page_service.get_failure_by_slug)
    def test_failure_get_single_page(self, mock_get_by_slug):
        rv = self.app.get('/page/my-post')

        self.assertEqual(rv.status_code, 404)
        mock_get_by_slug.assert_called_with('my-post')

    @mock.patch('app.pages.resources.PageList.service.get_by_title', side_effect=mock_page_service.get_failure_by_title)
    @mock.patch('app.pages.resources.PageList.service.save_update', side_effect=mock_page_service.save_update)
    def test_add_new_page(self, mock_save_update, mock_get_by_title):
        post_data = dict(title="Post 1", content="this is my post")
        json_page_data = json.dumps(post_data)
        rv = self.app.post('/page/', data=json_page_data)

        self.assertEqual(rv.status_code, 201)
        mock_get_by_title.assert_called_with("Post 1")
        assert mock_save_update.called

    @mock.patch('app.pages.resources.PageList.service.get_by_title', side_effect=mock_page_service.get_by_title)
    @mock.patch('app.pages.resources.PageList.service.save_update', side_effect=mock_page_service.save_update)
    def test_failure_add_existing_page(self, mock_save_update, mock_get_by_title):
        post_data = dict(title="Post 1", content="this is my post")
        json_page_data = json.dumps(post_data)
        rv = self.app.post('/page/', data=json_page_data)

        self.assertEqual(rv.status_code, 409)
        mock_get_by_title.assert_called_with("Post 1")
        assert not mock_save_update.called

    @mock.patch('app.pages.resources.PageList.service.get_by_title', side_effect=mock_page_service.get_by_title)
    @mock.patch('app.pages.resources.PageList.service.save_update', side_effect=mock_page_service.save_update)
    def test_failure_add_invalid_page(self, mock_save_update, mock_get_by_title):
        post_data = dict(title="Post 1")
        json_page_data = json.dumps(post_data)
        rv = self.app.post('/page/', data=json_page_data)

        self.assertEqual(rv.status_code, 400)
        assert not mock_get_by_title.called
        assert not mock_save_update.called

    @mock.patch('app.pages.resources.PageDetail.service.get_by_slug', side_effect=mock_page_service.get_by_slug)
    @mock.patch('app.pages.resources.PageDetail.service.save_update', side_effect=mock_page_service.save_update)
    def test_update_page(self, mock_save_update, mock_get_by_slug):
        post_data = dict(title="Post 1", content="this is a modified content")
        json_page_data = json.dumps(post_data)
        rv = self.app.put('/page/post-1', data=json_page_data)

        self.assertEqual(rv.status_code, 200)
        mock_get_by_slug.assert_called_with("post-1")
        assert mock_save_update.called

    @mock.patch('app.pages.resources.PageDetail.service.get_by_slug', side_effect=mock_page_service.get_failure_by_slug)
    @mock.patch('app.pages.resources.PageDetail.service.save_update', side_effect=mock_page_service.save_update)
    def test_failure_update_not_existing_page(self, mock_save_update, mock_get_by_slug):
        post_data = dict(title="Post 1", content="this is a modified content")
        json_page_data = json.dumps(post_data)
        rv = self.app.put('/page/post-1', data=json_page_data)

        self.assertEqual(rv.status_code, 404)
        mock_get_by_slug.assert_called_with("post-1")
        assert not mock_save_update.called

    @mock.patch('app.pages.resources.PageDetail.service.get_by_slug', side_effect=mock_page_service.get_by_slug)
    @mock.patch('app.pages.resources.PageDetail.service.save_update', side_effect=mock_page_service.save_update)
    def test_failure_update_invalid_page(self, mock_save_update, mock_get_by_slug):
        post_data = dict(title="Post 1")
        json_page_data = json.dumps(post_data)
        rv = self.app.put('/page/post-1', data=json_page_data)

        self.assertEqual(rv.status_code, 400)
        mock_get_by_slug.assert_called_with("post-1")
        assert not mock_save_update.called

    @mock.patch('app.pages.resources.PageDetail.service.get_by_slug', side_effect=mock_page_service.get_by_slug)
    @mock.patch('app.pages.resources.PageDetail.service.delete', side_effect=mock_page_service.delete)
    def test_delete_page(self, mock_delete, mock_get_by_slug):
        rv = self.app.delete('/page/post-1')

        self.assertEqual(rv.status_code, 204)
        mock_get_by_slug.assert_called_with("post-1")
        assert mock_delete.called

    @mock.patch('app.pages.resources.PageDetail.service.get_by_slug', side_effect=mock_page_service.get_failure_by_slug)
    @mock.patch('app.pages.resources.PageDetail.service.delete', side_effect=mock_page_service.delete)
    def test_failure_delete_page(self, mock_delete, mock_get_by_slug):
        rv = self.app.delete('/page/post-1')

        self.assertEqual(rv.status_code, 404)
        mock_get_by_slug.assert_called_with("post-1")
        assert not mock_delete.called
