from flask import Flask, jsonify
import os, requests
app=Flask(__name__); COMFYUI_URL=os.getenv('COMFYUI_URL','http://127.0.0.1:8188').rstrip('/')
def online():
 try:return requests.get(COMFYUI_URL+'/system_stats',timeout=3).ok
 except:return False
@app.get('/api/health')
def health():return jsonify(ok=True,service='FLOW FILIPINO AI SERVER',version='6.1',local_no_credit_engine='WAN 2.1 + ComfyUI',comfyui_online=online())
@app.get('/api/engine/status')
def status():return jsonify(wan_local={'label':'WAN LOCAL — NO CREDIT REQUIRED','available':online()},gemini_omni={'label':'GEMINI OMNI — CLOUD','available':bool(os.getenv('GEMINI_API_KEY'))},veo={'label':'VEO — CLOUD','available':bool(os.getenv('GOOGLE_CLOUD_PROJECT'))})
@app.get('/')
def root():return jsonify(ok=True,service='FLOW FILIPINO AI SERVER',version='6.1')
if __name__=='__main__':app.run(host='0.0.0.0',port=int(os.getenv('PORT','3000')))
