from google.adk.agents.llm_agent import Agent
from datetime import datetime
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pytz

def get_current_time(city: str) -> dict:
    """Returns the current real current time in any city in the world."""
    
    try:
        # Get coordinates of the city
        geolocator = Nominatim(user_agent="adk_time_agent")
        location = geolocator.geocode(city)
        
        if not location:
            return {
                "status": "error",
                "message": f"Could not find city: {city}"
            }
        
        # Find timezone from coordinates
        tf = TimezoneFinder()
        timezone_str = tf.timezone_at(
            lat=location.latitude, 
            lng=location.longitude
        )
        
        # Get real current time
        timezone = pytz.timezone(timezone_str)
        current_time = datetime.now(timezone)
        formatted_time = current_time.strftime("%I:%M %p, %A %d %B %Y")
        
        return {
            "status": "success",
            "city": city,
            "time": formatted_time,
            "timezone": timezone_str
        }
    
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description="Tells the real current time in any city in the world.",
    instruction="You are a helpful assistant that tells the current time in any city in the world. Use the 'get_current_time' tool for this purpose. Always mention the timezone along with the time.",
    tools=[get_current_time],
)