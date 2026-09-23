# Launch note: new sign-in page

## What changed

Starting Wednesday, the sign-in page asks for the email first. The password moves to the next step.

- The email field is first and full width.
- "Forgot password?" moves to the password step.
- Single sign-on users skip the password step.

## When it ships

Wednesday at noon, behind the `new-sign-in` flag. The flag goes to 10% of users first, then to everyone by 17:00.

## Who does what

- **Design:** final copy by Tuesday.
- **Engineering:** turns on the flag on Wednesday at noon.
- **Support:** publishes the help article on Wednesday afternoon.

## Rollback

If sign-ins drop more than 5% in the first hour, engineering turns the flag off. The old page comes back right away, with no deploy.
