const fs = require('fs');
const path = require('path');

const tourBtnKeys = {
  en: {
    "skip_tour": "Skip Tour",
    "back": "Back",
    "next": "Next →",
    "finish": "🎉 Finish"
  },
  hi: {
    "skip_tour": "टूर छोड़ें",
    "back": "पीछे",
    "next": "आगे →",
    "finish": "🎉 समाप्त"
  },
  mr: {
    "skip_tour": "टूर सोडा",
    "back": "मागे",
    "next": "पुढे →",
    "finish": "🎉 समाप्त"
  }
};

for (const [lang, keys] of Object.entries(tourBtnKeys)) {
  const filePath = path.join(__dirname, 'frontend', 'public', 'locales', lang, 'translation.json');
  const content = fs.readFileSync(filePath, 'utf8');
  const data = JSON.parse(content);
  Object.assign(data, keys);
  fs.writeFileSync(filePath, JSON.stringify(data, null, 2) + '\n');
  console.log('Updated', filePath);
}
