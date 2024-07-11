mkdir -p ~/.streamlit/

echo "\
[server]In
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml