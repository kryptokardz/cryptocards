"""Test for login and registration."""
from django.core import mail
from django.test import TestCase
from django.urls import reverse_lazy
from django.contrib.auth.models import User
import factory


class UserFactory(factory.django.DjangoModelFactory):
    """Factory for fake User."""

    class Meta:
        """Meta."""

        model = User

    username = factory.Sequence(lambda n:
                                '{}{}'.format(factory.Faker('first_name'), n))
    email = factory.Faker('email')


class MainRoutingTests(TestCase):
    """Tests for the routes in imagersite."""

    def setUp(self):
        """Set up a user for testing login.."""
        user = UserFactory(username='bob', email='bob@bob.net')
        user.set_password('password')
        user.save()

    def test_login_get_has_200_response(self):
        """Test that login get route has a 200 response code."""
        response = self.client.get(reverse_lazy('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_get_login_form(self):
        """Test that login get route has a login form."""
        response = self.client.get(reverse_lazy('login'))
        self.assertIn(b'Login', response.content)

    def test_login_post_invalid_user_has_200_response(self):
        """Test that login with invalid username has a 200 response code."""
        response = self.client.post(reverse_lazy('login'), {
            'username': 'fred',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 200)

    def test_login_post_invalid_user_displays_invalid_login(self):
        """Test that login with invalid username displays to bad login."""
        response = self.client.post(reverse_lazy('login'), {
            'username': 'fred',
            'password': 'password'
        })
        self.assertIn(b'Please enter a correct username and password', response.content)

    def test_login_post_invalid_password_has_200_response(self):
        """Test that login with invalid username has a 200 response code."""
        response = self.client.post(reverse_lazy('login'), {
            'username': 'bob',
            'password': 'passwordssss'
        })
        self.assertEqual(response.status_code, 200)

    def test_login_post_invalid_password_displays_invalid_login(self):
        """Test that login with invalid username displays to bad login."""
        response = self.client.post(reverse_lazy('login'), {
            'username': 'bob',
            'password': 'passwordssss'
        })
        self.assertIn(b'Note that both fields may be case-sensitive.', response.content)

    def test_login_post_valid_login_has_302_response(self):
        """Test that login with valid login has a 302 response code."""
        response = self.client.post(reverse_lazy('login'), {
            'username': 'bob',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 302)

    def test_login_post_validates_users(self):
        """Test that login validates users."""
        response = self.client.get(reverse_lazy('home'))
        self.assertNotIn(b'Welcome,', response.content)
        self.client.post(reverse_lazy('login'), {
            'username': 'bob',
            'password': 'password'
        })
        response = self.client.get(reverse_lazy('home'))
        self.assertIn(b' <h1>Cryptomonsters</h1>', response.content)

    def test_login_post_valid_login_redirects_to_profile_page(self):
        """Test that login with valid login redirects to home page."""
        response = self.client.post(reverse_lazy('login'), {
            'username': 'bob',
            'password': 'password'
        }, follow=True)
        self.assertEqual(response.redirect_chain[0][0], '/')

    def test_logout_get_has_200_response(self):
        """Test that logout get route has a 200 response code."""
        response = self.client.get(reverse_lazy('logout'))
        self.assertEqual(response.status_code, 302)

    # def test_logout_get_has_logged_out_title(self):
    #     """Test that logout get route has logged-out title."""
    #     response = self.client.get(reverse_lazy('logout'))
    #     self.assertIn(b' <h1>Cryptomonsters</h1>', response.content)

    def test_logout_from_login_user_will_logsout_user(self):
        """Test that logout will redirects to logout page."""
        self.client.login(username='bob', password='password')
        response = self.client.get(reverse_lazy('home'))
        self.assertIn(b' <h1>Cryptomonsters</h1>', response.content)
        self.client.get(reverse_lazy('logout'))
        response = self.client.get(reverse_lazy('home'))
        self.assertNotIn(b'Welcome,', response.content)

    def test_register_get_has_200_response(self):
        """Test that register get route has a 200 response code."""
        response = self.client.get(reverse_lazy('registration_register'))
        self.assertEqual(response.status_code, 200)

    def test_register_get_has_register_form(self):
        """Test that register get route has registration form."""
        response = self.client.get(reverse_lazy('registration_register'))
        self.assertIn(b'Enter the same password as before', response.content)

    def test_register_valid_user_password_gets_302_response(self):
        """Test if valid user with password responds with 302."""
        response = self.client.post(reverse_lazy('registration_register'), {
            'username': 'Rob',
            'password1': 'Codefellows',
            'password2': 'Codefellows',
            'email': 'rob@email.com'
        })
        self.assertEqual(response.status_code, 302)

    def test_register_redirects_to_registration_complete_page(self):
        """Test register redirects to registration complate page."""
        response = self.client.post(reverse_lazy('registration_register'), {
            'username': 'Rob',
            'password1': 'Codefellows',
            'password2': 'Codefellows',
            'email': 'rob@email.com'
        }, follow=True)
        self.assertIn(b'<title>Cryptomonsters</title>', response.content)

    def test_register_valid_user_password_creates_inactive_user(self):
        """Test if valid user with password creates a new inactive user."""
        self.client.post(reverse_lazy('registration_register'), {
            'username': 'Rob',
            'password1': 'Codefellows',
            'password2': 'Codefellows',
            'email': 'rob@email.com'
        })
        self.assertEqual(User.objects.count(), 2)
        self.assertFalse(User.objects.get(username='Rob').is_active)

    def test_register_will_send_email_after_registration(self):
        """Test registration will send Email after Registartion."""
        self.client.post(reverse_lazy('registration_register'), {
            'username': 'Rob',
            'password1': 'Codefellows',
            'password2': 'Codefellows',
            'email': 'rob@email.com'
        })
        self.assertEqual(len(mail.outbox), 1)

    def test_register_will_send_email_and_link_after_registration(self):
        """Test registration will send Email and link after Registartion."""
        self.client.post(reverse_lazy('registration_register'), {
            'username': 'Rob',
            'password1': 'Codefellows',
            'password2': 'Codefellows',
            'email': 'rob@email.com'
        })
        self.assertIn('/accounts/activate/', mail.outbox[0].body)

    def test_actvation_link_redirects_to_activate_complated_page(self):
        """Test if Acitvation link works."""
        import re
        self.client.post(reverse_lazy('registration_register'), {
            'username': 'Rob',
            'password1': 'Codefellows',
            'password2': 'Codefellows',
            'email': 'rob@email.com'
        })
        activation = re.findall('/accounts/activate/.+/', mail.outbox[0].body)
        response = self.client.get(activation[0], follow=True)
        self.assertIn(b'Thank you! Your account is now active!', response.content)

    def test_register_with_activation_valid_user_password_activates_user(self):
        """Test if valid user with password is activated, activates user."""
        import re
        self.client.post(reverse_lazy('registration_register'), {
            'username': 'Rob',
            'password1': 'Codefellows',
            'password2': 'Codefellows',
            'email': 'rob@email.com'
        })
        activation = re.findall('/accounts/activate/.+/', mail.outbox[0].body)
        self.client.get(activation[0])
        self.assertTrue(User.objects.get(username='Rob').is_active)

    def test_register_taken_username_responds_with_200(self):
        """Test register taken responds with 200."""
        response = self.client.post(reverse_lazy('registration_register'), {
            'username': 'bob',
            'password1': 'Codefellows',
            'password2': 'Codefellows',
            'email': 'bob@email.com'
        })
        self.assertEqual(200, response.status_code)

    def test_register_taken_user_name_displays_name_taken(self):
        """Test register taken responds with username taken."""
        response = self.client.post(reverse_lazy('registration_register'), {
            'username': 'bob',
            'password1': 'Codefellows',
            'password2': 'Codefellows',
            'email': 'bob@email.com'
        })
        self.assertIn(b'username already exists', response.content)

    def test_profile_view_shows_username(self):
        """Test username on profile page after login."""
        self.client.post(reverse_lazy('login'), {
            'username': 'bob',
            'password': 'password'
        }, follow=True)
        response = self.client.get(reverse_lazy('profile'))
        self.assertIn(b'<p><strong>email:</strong> bob@bob.net</p>',
                      response.content)

    def test_user_template_used_on_update_page(self):
        """Test successful user update redirects to profile page."""
        self.client.post(reverse_lazy('login'), {
            'username': 'bob',
            'password': 'password'
        }, follow=True)
        response = self.client.get(reverse_lazy('updateuser'))
        self.assertTemplateUsed(response,
                                'cryptomonsters/user_update_form.html')

    def test_user_update_redirects_to_profile(self):
        """Test successful user update redirects to profile page."""
        self.client.post(reverse_lazy('login'), {
            'username': 'bob',
            'password': 'password'
        }, follow=True)
        response = self.client.post(reverse_lazy('updateuser'), {
            'email': 'boberino@bob.com'
        }, follow=True)
        self.assertTemplateUsed(response, 'cryptomonsters/profile.html')

    def test_update_user_info(self):
        """Test username on profile page after login."""
        self.client.post(reverse_lazy('login'), {
            'username': 'bob',
            'password': 'password'
        }, follow=True)
        response = self.client.post(reverse_lazy('updateuser'), {
            'email': 'boberino@bob.com'
        }, follow=True)
        self.assertIn(b'boberino@bob.com', response.content)

    def test_update_user_if_not_logged_in_redirects_to_login(self):
        """Test update user page redirects to login if not logged in."""
        response = self.client.get(reverse_lazy('updateuser'), follow=True)
        self.assertTemplateUsed(response,
                                'registration/login.html')
