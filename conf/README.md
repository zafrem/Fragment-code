# conf - Configuration Files

This directory contains configuration files and settings for various services and APIs used throughout the Fragment Code repository.

## 📁 Configuration Files

### 🔑 configure.ini
Main configuration file containing API keys and service settings.

**Structure:**
```ini
[Token]
Open_API_Key = YOUR_API_KEY_HERE
```

**Purpose:**
- Centralized API key management
- Service authentication credentials
- Environment-specific settings

## 🔧 Setup Instructions

### 1. API Key Configuration
Replace placeholder values in `configure.ini` with your actual API keys:

```ini
[Token]
Open_API_Key = your_actual_api_key_here

[FRED]
API_Key = your_fred_api_key

[OpenWeather]
API_Key = your_openweather_api_key

[News]
API_Key = your_news_api_key
```

### 2. Environment Variables (Recommended)
For better security, use environment variables instead of storing keys in files:

```bash
export OPEN_API_KEY="your_api_key"
export FRED_API_KEY="your_fred_key"
export OPENWEATHER_API_KEY="your_weather_key"
export NEWS_API_KEY="your_news_key"
```

### 3. Python Configuration Loading
Example of how to load configuration in your scripts:

```python
import configparser
import os

# Method 1: Load from config file
config = configparser.ConfigParser()
config.read('conf/configure.ini')
api_key = config['Token']['Open_API_Key']

# Method 2: Load from environment variables (recommended)
api_key = os.getenv('OPEN_API_KEY')
```

## 🔒 Security Best Practices

### ⚠️ Important Security Notes

1. **Never commit real API keys** to version control
2. **Use environment variables** for production deployments
3. **Rotate keys regularly** and update configurations
4. **Limit API key permissions** to minimum required scope

### Git Security
Add sensitive files to `.gitignore`:
```gitignore
conf/configure.ini
.env
*.key
secrets/
```

### Production Deployment
- Use secret management services (AWS Secrets Manager, Azure Key Vault)
- Implement key rotation policies
- Monitor API usage and set alerts
- Use different keys for development/staging/production

## 📋 Required API Services

### Commonly Used APIs
Based on the repository modules, you'll need keys for:

- **FRED API** - Economic data from Federal Reserve
- **OpenWeather API** - Weather data and forecasts
- **News APIs** - Various news aggregation services
- **Financial APIs** - Stock market and economic data
- **Blog APIs** - Content management and extraction

### Getting API Keys

1. **FRED (Federal Reserve Economic Data)**
   - Visit: https://fred.stlouisfed.org/docs/api/api_key.html
   - Register for free API access

2. **OpenWeather**
   - Visit: https://openweathermap.org/api
   - Sign up for free tier (60 calls/minute)

3. **News APIs**
   - NewsAPI.org - https://newsapi.org/
   - Various RSS feeds (no key required)

## 🔄 Configuration Management

### Development vs Production
```ini
[Development]
Debug = True
Log_Level = DEBUG
Rate_Limit = False

[Production]
Debug = False
Log_Level = ERROR
Rate_Limit = True
```

### Service-Specific Settings
```ini
[FRED]
API_Key = your_fred_key
Base_URL = https://api.stlouisfed.org/fred/
Format = json
Rate_Limit = 120  # requests per minute

[OpenWeather]
API_Key = your_weather_key
Base_URL = https://api.openweathermap.org/data/2.5/
Units = metric
Language = en
```

## 🛠️ Troubleshooting

### Common Issues
- **401 Unauthorized** - Check API key validity
- **403 Forbidden** - Verify API key permissions
- **429 Too Many Requests** - Implement rate limiting
- **Connection Errors** - Check network and service status

### Debugging Tips
```python
# Test API connectivity
import requests

def test_api_connection(api_key):
    try:
        response = requests.get(f"https://api.example.com/test?key={api_key}")
        return response.status_code == 200
    except Exception as e:
        print(f"Connection failed: {e}")
        return False
```

---

*Secure, centralized configuration management for all your API integrations.*