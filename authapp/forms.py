from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    """ Can be used during signup to ask the user for additional input (e.g. newsletter signup, birth date).
    This class should implement a def signup(self, request, user) method, where user represents the newly signed up user.
    """

    def save(self, request):
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(CustomSignupForm, self).save(request)

        # Add your own processing here.

        # You must return the original result.
        return user
