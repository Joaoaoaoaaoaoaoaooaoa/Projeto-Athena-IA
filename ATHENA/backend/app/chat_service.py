from backend.core.intelligence.intent import IntentDetector


class ChatService:
    def __init__(self):
        self.intent_detector = IntentDetector()

    def process_message(self, message: str) -> str:
        intent = self.intent_detector.detect(message)

        if intent == "greeting":
            return "Olá! Eu sou a ATHENA."

        return f"Ainda não sei como responder a isso. Intenção: {intent}"