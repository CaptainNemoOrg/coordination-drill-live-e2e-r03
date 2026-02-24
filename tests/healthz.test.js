import { describe, it, expect } from 'vitest';

describe('Health Check', () => {
  it('should return ok true and version', async () => {
    const http = await import('http');
    
    const res = await new Promise((resolve) => {
      const req = http.get('http://localhost:3456/healthz', (res) => {
        let data = '';
        res.on('data', chunk => data += chunk);
        res.on('end', () => resolve({ status: res.statusCode, body: JSON.parse(data) }));
      });
      req.end();
    });
    
    expect(res.status).toBe(200);
    expect(res.body.ok).toBe(true);
    expect(res.body.version).toBe('1.0.0');
  });
});
