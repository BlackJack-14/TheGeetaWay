#!/usr/bin/env python3
"""
TheGeetaWay API Key Generator
Generate secure API keys for TheGeetaWay API authentication

Usage:
    python generate_api_key.py                 # Generate one key
    python generate_api_key.py --count 5       # Generate 5 keys
    python generate_api_key.py --update-env    # Generate and update .env file
"""

import secrets
import string
import argparse
import os
from pathlib import Path
from datetime import datetime


def generate_api_key(length: int = 32, prefix: str = "") -> str:
    """
    Generate a cryptographically secure API key
    
    Args:
        length: Length of the random part (default: 32)
        prefix: Optional prefix (e.g., "prod_", "dev_")
    
    Returns:
        Secure API key string
    """
    random_part = secrets.token_urlsafe(length)
    
    if prefix:
        return f"{prefix}{random_part}"
    return random_part


def generate_hex_key(length: int = 32) -> str:
    """Generate hex-encoded key"""
    return secrets.token_hex(length)


def generate_alphanumeric_key(length: int = 32) -> str:
    """Generate alphanumeric key"""
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))


def update_env_file(api_key: str, env_path: str = ".env"):
    """
    Update or create .env file with new API key
    
    Args:
        api_key: The API key to set
        env_path: Path to .env file
    """
    env_file = Path(env_path)
    
    if env_file.exists():
        with open(env_file, 'r') as f:
            lines = f.readlines()
        
        updated = False
        new_lines = []
        for line in lines:
            if line.startswith('API_KEY='):
                new_lines.append(f'API_KEY={api_key}\n')
                updated = True
            else:
                new_lines.append(line)
        
        if not updated:
            new_lines.append(f'\nAPI_KEY={api_key}\n')
        
        with open(env_file, 'w') as f:
            f.writelines(new_lines)
        
        print(f"✅ Updated {env_path} with new TheGeetaWay API key")
    
    else:
        with open(env_file, 'w') as f:
            f.write(f"# TheGeetaWay - Your Path to Ancient Wisdom\n")
            f.write(f"# API Configuration\n")
            f.write(f"# Generated: {datetime.now().isoformat()}\n\n")
            f.write(f"# API Key for authentication\n")
            f.write(f"API_KEY={api_key}\n\n")
            f.write(f"# Groq API Key (get from https://console.groq.com)\n")
            f.write(f"GROQ_API_KEY=\n\n")
            f.write(f"# API Base URL (for frontend)\n")
            f.write(f"API_BASE_URL=http://localhost:8000\n\n")
            f.write(f"# Allowed CORS origins (comma-separated)\n")
            f.write(f"ALLOWED_ORIGINS=http://localhost:8501,http://localhost:3000\n")
        
        print(f"✅ Created {env_path} with TheGeetaWay configuration")


def display_key_info(key: str):
    """Display key information"""
    print("\n" + "=" * 70)
    print("🪔 THEGEETAWAY API KEY")
    print("=" * 70)
    print(f"\n{key}\n")
    print("=" * 70)
    print("\n📋 Key Information:")
    print(f"   Length: {len(key)} characters")
    print(f"   Entropy: ~{len(key) * 6} bits")
    print(f"   Type: URL-safe Base64")
    print("\n🔒 Security Guidelines:")
    print("   • Never commit this key to version control")
    print("   • Store it in .env file (add .env to .gitignore)")
    print("   • Rotate keys every 90 days for security")
    print("   • Use different keys for dev/staging/prod")
    print("   • Never share keys via email or chat")
    print("\n📝 How to Use:")
    print("   • Backend: Add to .env → API_KEY=" + key)
    print("   • Frontend: Add to .env → API_KEY=" + key)
    print("   • API Call: Add header → X-API-Key: " + key)
    print("\n🎯 Next Steps:")
    print("   1. Add your GROQ_API_KEY to .env")
    print("   2. Start TheGeetaWay API: uvicorn api:app --reload")
    print("   3. Start Streamlit: streamlit run app.py")
    print("=" * 70 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="Generate secure API keys for TheGeetaWay",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
TheGeetaWay - Your Path to Ancient Wisdom

Examples:
  python generate_api_key.py
  python generate_api_key.py --count 5
  python generate_api_key.py --update-env
  python generate_api_key.py --prefix prod_ --update-env
  python generate_api_key.py --type hex --length 64

For more information: https://thegeetaway.com/docs
        """
    )
    
    parser.add_argument(
        '--count', '-c',
        type=int,
        default=1,
        help='Number of keys to generate (default: 1)'
    )
    
    parser.add_argument(
        '--length', '-l',
        type=int,
        default=32,
        help='Length of the key (default: 32)'
    )
    
    parser.add_argument(
        '--prefix', '-p',
        type=str,
        default='',
        help='Prefix for the key (e.g., prod_, dev_, staging_)'
    )
    
    parser.add_argument(
        '--type', '-t',
        choices=['urlsafe', 'hex', 'alphanumeric'],
        default='urlsafe',
        help='Type of key to generate (default: urlsafe)'
    )
    
    parser.add_argument(
        '--update-env',
        action='store_true',
        help='Update .env file with generated key'
    )
    
    parser.add_argument(
        '--env-file',
        type=str,
        default='.env',
        help='Path to .env file (default: .env)'
    )
    
    parser.add_argument(
        '--quiet', '-q',
        action='store_true',
        help='Only output the key (no formatting)'
    )
    
    args = parser.parse_args()
    
    # Generate keys
    keys = []
    for i in range(args.count):
        if args.type == 'hex':
            key = generate_hex_key(args.length)
        elif args.type == 'alphanumeric':
            key = generate_alphanumeric_key(args.length)
        else:  # urlsafe
            key = generate_api_key(args.length, args.prefix)
        
        keys.append(key)
    
    # Output
    if args.quiet:
        for key in keys:
            print(key)
    else:
        if args.count == 1:
            display_key_info(keys[0])
            
            if args.update_env:
                update_env_file(keys[0], args.env_file)
        else:
            print("\n" + "=" * 70)
            print(f"🪔 THEGEETAWAY - GENERATED {args.count} API KEYS")
            print("=" * 70 + "\n")
            for i, key in enumerate(keys, 1):
                env_suffix = ""
                if args.prefix:
                    if "prod" in args.prefix:
                        env_suffix = " (Production)"
                    elif "staging" in args.prefix:
                        env_suffix = " (Staging)"
                    elif "dev" in args.prefix:
                        env_suffix = " (Development)"
                
                print(f"Key {i}{env_suffix}: {key}")
            print("\n" + "=" * 70 + "\n")


if __name__ == "__main__":
    main()