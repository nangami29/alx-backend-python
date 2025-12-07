from datetime import datetime, timedelta
from django.http import HttpResponseForbidden,  JsonResponse

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
       
        user = request.user if request.user.is_authenticated else "Anonymous"

        log_message = f"{datetime.now()} - User: {user} - Path: {request.path}"

        with open('requests.log', 'a') as file:
            file.write(log_message + '\n')

        return self.get_response(request)

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        current_hour=datetime.now().hour
        if current_hour< 9 or current_hour>18:
            return HttpResponseForbidden("Access Denied")

        return self.get_response(request)
    
class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_tracker = {}    
        self.limit = 5                
        self.time_window = 60       

    def __call__(self, request):
        # Only monitor POST requests (messages)
        if request.method == "POST":
            ip = request.META.get('REMOTE_ADDR', 'UNKNOWN')
            now = datetime.now()

            # Create entry if IP not tracked before
            if ip not in self.requests_tracker:
                self.requests_tracker[ip] = []

            # Keep only timestamps within last 60 seconds
            self.requests_tracker[ip] = [
                t for t in self.requests_tracker[ip]
                if now - t < timedelta(seconds=self.time_window)
            ]

            
            if len(self.requests_tracker[ip]) >= self.limit:
                return JsonResponse(
                    {"error": "Message limit exceeded. Only 5 messages allowed per minute."},
                    status=429
                )

        self.requests_tracker[ip].append(now)

       
        return self.get_response(request)



# 2. RolePermissionMiddleware — Admin required


class RolepermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = getattr(request, "user", None)

        # If `user` is authenticated and has a "role" field
        if user and user.is_authenticated:
            role = getattr(user, "role", None)

            # Only "admin" or "moderator" allowed
            if role not in ["admin", "moderator"]:
                return JsonResponse(
                    {"error": "Forbidden: You do not have permission to access this resource."},
                    status=403
                )

        # Allow the request
        return self.get_response(request)