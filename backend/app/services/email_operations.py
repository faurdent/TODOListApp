from fastapi_mail import FastMail, MessageSchema, MessageType

from app.core.config import connection_config
from app.crud import verification_code


async def send_verification_code(db, user_id, email):
    verification_user_code = await verification_code.create_or_update_verification_code(db, user_id)
    fast_mail = FastMail(connection_config)
    message_body = f"<p>Your code: {verification_user_code.verification_code}</p>" \
                   f"<a href='http://localhost:8000/users/" \
                   f"verify/{verification_user_code.verification_code}'>Verify account</a>"
    message = MessageSchema(
        subject="Account verification",
        recipients=[email],
        body=message_body,
        subtype=MessageType.html
    )
    await fast_mail.send_message(message)
