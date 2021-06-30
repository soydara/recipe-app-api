def test_create_user_page(self):
    """Test that the create user page works"""
    url = reverse('admin:core_user_add')
    res = self.client.get(url)

    self.assertEqual(res.status_code, 200)