
from waitress import serve
import SAFlaskFinal

serve(SAFlaskFinal.app, port=8000, threads=6)