const fs = require('fs');
const path = require('path');

const i18nPath = path.join(__dirname, 'frontend', 'src', 'i18n.js');
let code = fs.readFileSync(i18nPath, 'utf8');

// We will inject hi and mr directly into the `resources` object
const localesPath = path.join(__dirname, 'frontend', 'public', 'locales');
const enTranslations = JSON.parse(fs.readFileSync(path.join(localesPath, 'en', 'translation.json'), 'utf8'));
const hiTranslations = JSON.parse(fs.readFileSync(path.join(localesPath, 'hi', 'translation.json'), 'utf8'));
const mrTranslations = JSON.parse(fs.readFileSync(path.join(localesPath, 'mr', 'translation.json'), 'utf8'));

// 1. Locate the end of `resources` which currently holds `en`
// The structure is:
// const resources = {
//     en: {
//         translation: { ... }
//     }
// };

// Replace the entire resources block with a generated string holding all three:
const buildResources = () => {
    return `const resources = {
    en: { translation: ${JSON.stringify(enTranslations, null, 4)} },
    hi: { translation: ${JSON.stringify(hiTranslations, null, 4)} },
    mr: { translation: ${JSON.stringify(mrTranslations, null, 4)} }
};`;
};

// Find the regex to replace: const resources = { ... };
code = code.replace(/const resources = \{[\s\S]*?en: \{[\s\S]*?translation: \{[\s\S]*?\}\s*\}\s*\};/, buildResources());

// Write back to i18n.js
fs.writeFileSync(i18nPath, code);
console.log("Updated i18n.js with full inline translations for en, hi, mr.");
