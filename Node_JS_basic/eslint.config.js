// eslint.config.js
import js from '@eslint/js';
import globals from 'globals';
import eslintPluginJest from 'eslint-plugin-jest';
import airbnbBase from 'eslint-config-airbnb-base';

export default [
  js.configs.recommended,
  {
    files: ['**/*.js'],
    languageOptions: {
      ecmaVersion: 2018,
      sourceType: 'module',
      globals: {
        ...globals.node,
        ...globals.es6,
        ...globals.jest,
        Atomics: 'readonly',
        SharedArrayBuffer: 'readonly',
      },
    },
    plugins: {
      jest: eslintPluginJest,
    },
    rules: {
      'max-classes-per-file': 'off',
      'no-underscore-dangle': 'off',
      'no-console': 'off',
      'no-shadow': 'off',
      'no-restricted-syntax': [
        'error',
        'LabeledStatement',
        'WithStatement',
      ],
      ...eslintPluginJest.configs.all.rules,
    },
    ignores: ['babel.config.js'],
  },
];
