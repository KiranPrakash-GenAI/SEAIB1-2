import streamlit as st
import requests

st.title("📅 3-Day Weather Forecast (No API Key)")

location = st.text_input("Enter location (e.g., Delhi, Tokyo):")

if st.button("Get Forecast"):
    if location:
        try:
            url = f"https://wttr.in/{location}?format=j1"
            response = requests.get(url)
            data = response.json()

            # Current
            current = data["current_condition"][0]
            st.subheader(f"🌤️ Current Weather - {location.title()}")
            st.write(f"Temperature: {current['temp_C']} °C")
            st.write(f"Feels Like: {current['FeelsLikeC']} °C")
            st.write(f"Condition: {current['weatherDesc'][0]['value']}")
            st.write(f"Humidity: {current['humidity']}%")
            st.write(f"Wind: {current['windspeedKmph']} km/h")

            st.markdown("---")

            # Forecast for 3 days
            st.subheader("🔮 3-Day Forecast")
            for day in data["weather"]:
                date = day["date"]
                maxtemp = day["maxtempC"]
                mintemp = day["mintempC"]
                sunrise = day["astronomy"][0]["sunrise"]
                sunset = day["astronomy"][0]["sunset"]
                description = day["hourly"][4]["weatherDesc"][0]["value"]  # Approx midday

                st.markdown(f"**📅 {date}**")
                st.write(f"🌞 Max Temp: {maxtemp} °C")
                st.write(f"🌙 Min Temp: {mintemp} °C")
                st.write(f"🌅 Sunrise: {sunrise}")
                st.write(f"🌇 Sunset: {sunset}")
                st.write(f"🌤️ Forecast: {description}")
                st.markdown("---")

        except Exception as e:
            st.error("⚠️ Failed to retrieve weather data.")
            st.exception(e)
    else:
        st.warning("Please enter a location.")
