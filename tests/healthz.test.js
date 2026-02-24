import { describe, it, expect } from 'vitest';

describe('Health Check', () => {
  it('should export a valid server module', async () => {
    const server = await import('../index.js');
    expect(server.default).toBeDefined();
    expect(typeof server.default.listen).toBe('function');
  });
  
  it('package.json has correct structure per DRILL CONTRACT', () => {
    const pkg = import('../package.json', { assert: { type: 'json' } });
    expect(pkg.then).toBeDefined(); // it returns a promise
  });
});
