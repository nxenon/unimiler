# Unimiler (Unicode Normalizer)
Normalize unicode for WAF XSS Protection bypassing purposes and testing if normalizing is being used.

# Usage
The tool is an interactive script:
    
    python3 unimiler.py

# Example

    Python3 unimiler.py

    Enter text to normalize:ⓓ
    NFC: '\u24d3'
    NFD: '\u24d3'
    NFKC: 'd'
    NFKD: 'd'
    Enter text to normalize:ⓗ
    NFC: '\u24d7'
    NFD: '\u24d7'
    NFKC: 'h'
    NFKD: 'h'
    Enter text to normalize:𝐊
    NFC: '\U0001d40a'
    NFD: '\U0001d40a'
    NFKC: 'K'
    NFKD: 'K'
