#include "stdafx.h"
#include "key_macro.h"
#include "key_macroDlg.h"
#include "DialogMacroEdit.h"
#include "DialogMacroRec.h"
#include "macro_def.h"
#include "macro_file.h"
#include "key_hook.h"
#include "virtual_key.h"
#include "AppIni.h"
#include "common.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

static bool _macro_changed = false;
Ckey_macroDlg *g_macroDlg = NULL;


// Ckey_macroDlg ��ȭ ����
Ckey_macroDlg::Ckey_macroDlg(CWnd* pParent /*=NULL*/)
	: CDialogCommon(Ckey_macroDlg::IDD, pParent)
{
	_macro_exec_time = 0;

	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);

	g_macroDlg = this;
}

Ckey_macroDlg::~Ckey_macroDlg()
{
	g_macroDlg = NULL;
}

void Ckey_macroDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	DDX_Control(pDX, IDC_LIST_MACROS, _listMacros);
	DDX_Control(pDX, IDC_LIST_MACROS2, _listMacros2);
	DDX_Control(pDX, IDC_STATIC_HOMEPAGE, _staticHomepage);
}

BEGIN_MESSAGE_MAP(Ckey_macroDlg, CDialog)
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	//}}AFX_MSG_MAP
	ON_WM_INPUT()
	ON_WM_DESTROY()
	ON_WM_TIMER()
	ON_BN_CLICKED(IDOK, &Ckey_macroDlg::OnBnClickedOk)
	ON_BN_CLICKED(IDCANCEL, &Ckey_macroDlg::OnBnClickedCancel)
	ON_BN_CLICKED(IDC_RADIO_MACRO_RUN, &Ckey_macroDlg::OnBnClickedRadioRun)
	ON_BN_CLICKED(IDC_RADIO_MACRO_EDIT, &Ckey_macroDlg::OnBnClickedRadioEdit)
	ON_BN_CLICKED(IDC_BUTTON_ADD_MACRO, &Ckey_macroDlg::OnBnClickedButtonAddMacro)
	ON_BN_CLICKED(IDC_BUTTON_COPY_MACRO, &Ckey_macroDlg::OnBnClickedButtonCopyMacro)
	ON_BN_CLICKED(IDC_BUTTON_DELETE_MACRO, &Ckey_macroDlg::OnBnClickedButtonDeleteMacro)
	ON_BN_CLICKED(IDC_BUTTON_EDIT_MACRO, &Ckey_macroDlg::OnBnClickedButtonEditMacro)
	ON_BN_CLICKED(IDC_BUTTON_MACRO_FILE, &Ckey_macroDlg::OnBnClickedButtonMacroFile)
	ON_BN_CLICKED(IDC_BUTTON_REC_MACRO, &Ckey_macroDlg::OnBnClickedButtonRecMacro)
	ON_BN_CLICKED(IDC_BUTTON_UP, &Ckey_macroDlg::OnBnClickedButtonUp)
	ON_BN_CLICKED(IDC_BUTTON_DOWN, &Ckey_macroDlg::OnBnClickedButtonDown)
	ON_BN_CLICKED(IDC_BUTTON_SAVE, &Ckey_macroDlg::OnBnClickedButtonSave)
	ON_BN_CLICKED(IDC_BUTTON_QUIT, &Ckey_macroDlg::OnBnClickedButtonQuit)
	ON_LBN_DBLCLK(IDC_LIST_MACROS, &Ckey_macroDlg::OnLbnDblclkListMacros)
	ON_CBN_SELCHANGE(IDC_COMBO_KEY, &Ckey_macroDlg::OnCbnSelchangeComboKey)
	ON_BN_CLICKED(IDC_CHECK_IME_HAN_ENG, &Ckey_macroDlg::OnBnClickedCheckImeHanEng)
	ON_BN_CLICKED(IDC_CHECK_RELEASE_ALL_KEY, &Ckey_macroDlg::OnBnClickedCheckReleaseAllKey)
END_MESSAGE_MAP()


// Ckey_macroDlg �޽��� ó����
BOOL Ckey_macroDlg::OnInitDialog()
{
	CDialog::OnInitDialog();

	// �� ��ȭ ������ �������� �����մϴ�. ���� ���α׷��� �� â�� ��ȭ ���ڰ� �ƴ� ��쿡��
	//  �����ӿ�ũ�� �� �۾��� �ڵ����� �����մϴ�.
	SetIcon(m_hIcon, TRUE);			// ū �������� �����մϴ�.
	SetIcon(m_hIcon, FALSE);		// ���� �������� �����մϴ�.

	// TODO: ���⿡ �߰� �ʱ�ȭ �۾��� �߰��մϴ�.
	SetWindowText (g_ini.macroProgramTitle);

	// Ÿ��Ʋ ��(ĸ�ǹ�)���� �����ư�� ��Ȱ��ȭ
	CMenu *pMenu = GetSystemMenu(FALSE);
	pMenu->RemoveMenu(SC_CLOSE, MF_BYCOMMAND);

	// �������� ��ġ�� �����Ѵ�.
	DlgInScreen (g_ini.windowSX, g_ini.windowSY);
	SetWindowPos (NULL, g_ini.windowSX, g_ini.windowSY, 0, 0, SWP_NOSIZE | SWP_NOZORDER);

	FillComboBoxVkList (IDC_COMBO_KEY, g_ini.keyMacroRun);

	// ���Ϸκ��� ��ũ�θ� �о����
	SetDlgItemText (IDC_EDIT_MACRO_FILE, g_ini.macroFileName);

	// ��ũ�ΰ� ó������ ���� ���°� �ǵ��� ���� ��ư ����
	CheckDlgButton (IDC_RADIO_MACRO_RUN,   BST_UNCHECKED);
	CheckDlgButton (IDC_RADIO_MACRO_EDIT,  BST_CHECKED);

	// ��ũ�� ���� �ɼ� 
	if (g_ini.eventDelay < 1) g_ini.eventDelay = 1;
	SetDlgItemInt (IDC_EDIT_EVENT_MIN_DELAY, g_ini.eventDelay, FALSE);
	CheckDlgButton (IDC_CHECK_IME_HAN_ENG,	    g_ini.macroOptions.CHECK_IME_HAN_ENG ? BST_CHECKED : BST_UNCHECKED);
	CheckDlgButton (IDC_CHECK_RELEASE_ALL_KEY,	g_ini.macroOptions.RELEASE_ALL_KEYS  ? BST_CHECKED : BST_UNCHECKED);

	// ���Ͽ��� ��ũ�θ� �ҷ��� ����Ʈ ��Ʈ�ѿ� ǥ���Ѵ�.
	LoadMacros (g_ini.macroFileName);

	_listMacros.ResetContent();
	for (unsigned int i=0; i<g_macros.size(); ++i) {
		_listMacros.InsertString (i, g_macros[i].name);
	}
	if (0 < g_macros.size()) {
		_listMacros.SetCurSel (0);
	}

	SetTextRecCount();

	// ���� ������ Ȩ������ �����۸�ũ ǥ��
	SetDlgItemText (IDC_STATIC_VERSION, GetVersionInfo("ProductVersion"));

	_staticHomepage.SetURL("https://blog.naver.com/pg365/223003862895");
	_staticHomepage.SetToolTipText("Ű����/���콺 ��ũ�� ���α׷� V1 (���� ����)");
	_staticHomepage.SetLinkCursor(::LoadCursor(0, MAKEINTRESOURCE(IDC_HAND)));

	// Ű����/���콺 �̺�Ʈ �� ��ġ
	const int RID_size = 2;
	RAWINPUTDEVICE rid[RID_size];
	ZeroMemory (rid, sizeof(RAWINPUTDEVICE)*RID_size);

	// Ű����
	rid[0].usUsagePage = 0x01;
	rid[0].usUsage = 0x06;
	rid[0].dwFlags = RIDEV_INPUTSINK;
	rid[0].hwndTarget = m_hWnd;

	// ���콺
	rid[1].usUsagePage = 0x01;
	rid[1].usUsage = 0x02;
	rid[1].dwFlags = RIDEV_INPUTSINK;
	rid[1].hwndTarget = m_hWnd;    //    �޽����� ó���� ���ν����� ������ �ڵ�

	if (!RegisterRawInputDevices (rid, RID_size, sizeof(RAWINPUTDEVICE))) {
		TRACE ("RegisterRawInputDevices Failed");
	}

	return TRUE;  // ��Ŀ���� ��Ʈ�ѿ� �������� ������ TRUE�� ��ȯ�մϴ�.
}

void Ckey_macroDlg::OnPaint()
{
	if (IsIconic()) {
		CPaintDC dc(this); // �׸��⸦ ���� ����̽� ���ؽ�Ʈ

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// Ŭ���̾�Ʈ �簢������ �������� ����� ����ϴ�.
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// �������� �׸��ϴ�.
		dc.DrawIcon(x, y, m_hIcon);
	}
	else {
		CDialog::OnPaint();
	}
}

HCURSOR Ckey_macroDlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}

void Ckey_macroDlg::OnDestroy()
{
	// ���� ���࿡ ��ũ�� ���α׷��� ��ġ�� �����ϱ� ���� ���� ��ġ�� ������ �д�.
	GetWindowsPos (g_ini.windowSX, g_ini.windowSY);

	CDialog::OnDestroy();
}

void Ckey_macroDlg::OnRawInput(UINT nInputcode, HRAWINPUT hRawInput)
{
	// This feature requires Windows XP or greater.
	// The symbol _WIN32_WINNT must be >= 0x0501.

	RAWINPUT rawInput;
    ZeroMemory (&rawInput, sizeof(RAWINPUT));
    
	UINT unSize = sizeof(RAWINPUT);
    ::GetRawInputData ((HRAWINPUT)hRawInput, RID_INPUT, &rawInput, &unSize, sizeof(RAWINPUTHEADER));

	switch (rawInput.header.dwType) {
    case RIM_TYPEKEYBOARD:
		OnRawKeyboard (rawInput.data.keyboard);
        break;
	case RIM_TYPEMOUSE: 
		OnRawMouse (rawInput.data.mouse);
		break; 
    case RIM_TYPEHID:
        break;
    default:
        break;
    }

	CDialog::OnRawInput(nInputcode, hRawInput);
}

void Ckey_macroDlg::OnTimer(UINT_PTR nIDEvent)
{
	if (nIDEvent == 1001) {
		DWORD current_time = GetTickCount ();
		AllMacroStep (current_time - _macro_exec_time);
		_macro_exec_time = current_time;
	}
	else if (nIDEvent == 1002) {
		for (unsigned int i=0; i<g_macros.size(); ++i) {
			_listMacros2.SetSel (i, g_macros[i].is_running());
		}
	}

	CDialog::OnTimer(nIDEvent);
}

void Ckey_macroDlg::OnKeybdMouseEvent (BYTE vk_code, bool vk_pressed)
{
	if (vk_code == g_ini.keyMacroRun && vk_pressed == true) {
		if (IsDlgButtonChecked (IDC_RADIO_MACRO_EDIT) == BST_CHECKED) {
			CheckDlgButton (IDC_RADIO_MACRO_RUN, BST_CHECKED);
			CheckDlgButton (IDC_RADIO_MACRO_EDIT, BST_UNCHECKED);

			OnBnClickedRadioRun();
		}
		else if (IsDlgButtonChecked (IDC_RADIO_MACRO_RUN) == BST_CHECKED) {
			CheckDlgButton (IDC_RADIO_MACRO_RUN, BST_UNCHECKED);
			CheckDlgButton (IDC_RADIO_MACRO_EDIT, BST_CHECKED);

			OnBnClickedRadioEdit();
		}
	}
	// ��ũ���� ���۰� ������ ���⼭�� �ϵ��� �Ѵ�.
	// ��, key_macroDlg â�� Ȱ��ȭ �Ǿ� ���� ���� ó���Ѵ�.
	MacroStartStopShortkey (vk_code, vk_pressed);
}

void Ckey_macroDlg::OnBnClickedButtonMacroFile()
{
	if (_macro_changed) {
		int ret = AfxMessageBox ("��ũ�ΰ� ����Ǿ����ϴ�. �����ұ��?", MB_YESNO|MB_ICONQUESTION);
		if (ret == IDYES) {
			OnBnClickedButtonSave ();
		}
	}

	///////////////////////////////////////////////////////////////////////////////
	char szFilter[] = "Macro file (*.m)|*.m|All Files(*.*)|*.*||";
	CFileDialog dlg(TRUE, NULL, g_ini.macroFileName, OFN_HIDEREADONLY, szFilter);
	
	if(IDOK == dlg.DoModal()) {
		char curPath[MAX_PATH+1] = "";
		GetCurrentDirectory (MAX_PATH, curPath);
		curPath[MAX_PATH] = '\0';

		CString fileNameNew = "";

		// ������ ��ΰ� ���� �۾���ο� ��ġ�ϸ�, �۾���δ� �����Ѵ�.
		if (strnicmp(curPath, (LPCSTR)dlg.GetPathName (), strlen(curPath)) == 0) {
			fileNameNew = (LPCSTR)dlg.GetPathName () + strlen(curPath) + 1;
		}
		else {
			fileNameNew = dlg.GetPathName();
		}
		// Ȯ���ڰ� ������ ".m" Ȯ���ڸ� ���δ�.
		if (dlg.GetFileExt ().GetLength () == 0) {
			fileNameNew += ".m";
		}

		// ���Ͽ� ����� ��ũ�� ���� �ҷ��´�.
		LoadMacros ((LPCSTR)fileNameNew);

		// �����쿡 ��ũ�� ��� ǥ��
		_listMacros.ResetContent();
		for (unsigned int i=0; i<g_macros.size(); ++i) {
			_listMacros.InsertString (i, g_macros[i].name);
		}
		_listMacros.SetCurSel(0);

		// ��ũ�� ���� �̸� ǥ��
		strncpy (g_ini.macroFileName, (LPCSTR)fileNameNew, MAX_PATH);
		g_ini.macroFileName[MAX_PATH] = '\0';
		SetDlgItemText (IDC_EDIT_MACRO_FILE, g_ini.macroFileName);
	}
}

void Ckey_macroDlg::EnableDlgItem(BOOL enable)
{
	GetDlgItem (IDC_COMBO_KEY)->EnableWindow (enable);
	GetDlgItem (IDC_BUTTON_REC_MACRO)->EnableWindow (enable);
	GetDlgItem (IDC_BUTTON_ADD_MACRO)->EnableWindow (enable);
	GetDlgItem (IDC_BUTTON_EDIT_MACRO)->EnableWindow (enable);
	GetDlgItem (IDC_BUTTON_COPY_MACRO)->EnableWindow (enable);
	GetDlgItem (IDC_BUTTON_DELETE_MACRO)->EnableWindow (enable);
	GetDlgItem (IDC_BUTTON_MACRO_FILE)->EnableWindow (enable);
	GetDlgItem (IDC_EDIT_EVENT_MIN_DELAY)->EnableWindow (enable);
	GetDlgItem (IDC_CHECK_IME_HAN_ENG)->EnableWindow (enable);
	GetDlgItem (IDC_CHECK_RELEASE_ALL_KEY)->EnableWindow (enable);
	GetDlgItem (IDC_BUTTON_UP)->EnableWindow (enable);
	GetDlgItem (IDC_BUTTON_DOWN)->EnableWindow (enable);
}

void Ckey_macroDlg::OnBnClickedOk()
{
	// Alt+F4, Esc Ű�� ���� ������ ����Ǵ� �� ����

	// OnOK();
}

void Ckey_macroDlg::OnBnClickedCancel()
{
	// Alt+F4, Esc Ű�� ���� ������ ����Ǵ� �� ����

	// OnCancel();
}

void Ckey_macroDlg::OnBnClickedRadioRun()
{
	if (g_macros.size() == 0) {
		AfxMessageBox ("��ϵ� ��ũ�ΰ� �����ϴ�.");
		return;
	}

	if (IsDlgButtonChecked (IDC_RADIO_MACRO_RUN) == BST_CHECKED) {
		// ��ũ�� ���� ��� ���·� �ٲ�
		MacroInit ();
		EnableDlgItem (FALSE);
		
		_listMacros2.ResetContent();

		// ��ũ�� ��Ͽ� ����/���� ���� ǥ��
		for (unsigned int i=0; i<g_macros.size(); ++i) {
			char buff[256+1];
			_snprintf (buff, 256, "%s (%s%s / %s%s)", 
				g_macros[i].name, 
				GetVkNameFromVK (g_macros[i].start_key & 0xFF),  
				(g_macros[i].start_key & VK_KEY_UP) ? "��" : "����",
				GetVkNameFromVK (g_macros[i].stop_key  & 0xFF),
				(g_macros[i].stop_key  & VK_KEY_UP) ? "��" : "����");
			buff[256] = '\0';

			_listMacros2.InsertString (i, buff);
		}

		_listMacros.ShowWindow (SW_HIDE);
		_listMacros2.ShowWindow (SW_SHOW);

		g_ini.eventDelay = GetDlgItemInt (IDC_EDIT_EVENT_MIN_DELAY, NULL, FALSE);
		g_ini.eventDelay = BOUND (g_ini.eventDelay, 1, 100000);

		// ��ũ�θ� �����ϵ��� Ÿ�̸� ����
		_macro_exec_time = GetTickCount ();
		SetTimer (1001, g_ini.eventDelay, NULL);	// ��ũ�θ� �����ϱ� ���� Ÿ�̸�
		SetTimer (1002, 33, NULL);					// ����Ǵ� ��ũ�θ� ����Ʈ �ڽ��� ǥ���ϱ� ���� Ÿ�̸�
	}
}

void Ckey_macroDlg::OnBnClickedRadioEdit()
{
	if (IsDlgButtonChecked (IDC_RADIO_MACRO_EDIT) == BST_CHECKED) {
		// ��ũ�� ���� ���·� �ٲ�
		MacroTerm ();

		EnableDlgItem (TRUE);

		_listMacros.ShowWindow (SW_SHOW);
		_listMacros2.ShowWindow (SW_HIDE);

		KillTimer (1001);
		KillTimer (1002);
	}
}

void Ckey_macroDlg::OnCbnSelchangeComboKey()
{
	int index = SendDlgItemMessage (IDC_COMBO_KEY, CB_GETCURSEL, 0, 0);
	if (index != -1) {
		g_ini.keyMacroRun = GetVkCode(index);
	}
}

void Ckey_macroDlg::SetTextRecCount()
{
	char text[256];

	sprintf (text, "%d�� ��ũ�ΰ� ��ϵ�.", g_macros.size());

	SetDlgItemText (IDC_STATIC_REC_COUNT, text);
}

void Ckey_macroDlg::OnBnClickedButtonAddMacro()
{
	CDialogMacroEdit dlg;

	// �߰��� ��ũ�θ� temp�� ����� �߰�(����) ��ȭ���ڿ� �Ѱ��ش�.
	// �߰� ��ȭ���ڿ��� OK ��ư�� ������ g_macros�� ������ ��ũ��(temp)�� �߰��Ѵ�.
	sMacro temp;
	dlg._macro = &temp;

	if (dlg.DoModal () == IDOK) {
		int count = _listMacros.GetCount ();

		_listMacros.InsertString (count, temp.name);
		_listMacros.SetCurSel (count);

		g_macros.push_back (temp);
		_macro_changed = true;
	}

	SetTextRecCount();
}

void Ckey_macroDlg::OnBnClickedButtonEditMacro()
{
	int sel = _listMacros.GetCurSel ();
	if (sel < 0) return;

	CDialogMacroEdit dlg;

	// ��ũ�θ� ������ ����, �����ϰ��� �ϴ� ��ũ�θ� temp�� �����Ͽ� ���� ��ȭ���ڷ� �Ѱ��ش�.
	// ���� ��ȭ���ڿ��� OK ��ư�� ������ ������ ��ũ��(temp)�� g_macros�� ��ϵ� ��ũ�ο� �����.
	sMacro temp = g_macros[sel];
	dlg._macro = &temp;

	if (dlg.DoModal () == IDOK) {
		_listMacros.DeleteString (sel);
		_listMacros.InsertString (sel, temp.name);
		_listMacros.SetCurSel (sel);

		g_macros[sel] = *dlg._macro;
		_macro_changed = true;
	}
}

void Ckey_macroDlg::OnBnClickedButtonRecMacro()
{
	CDialogMacroRec dlg;

	// ���� temp ��ũ�θ� �����, ����� ��ũ�θ� ����Ѵ�.
	// ��� ��ȭ���ڿ��� OK�� ������ temp�� ��ϵ� ��ũ�θ� g_macros�� �߰��Ѵ�.
	sMacro temp;
	dlg._macro = &temp;

	if (dlg.DoModal () == IDOK) {
		int count = _listMacros.GetCount ();

		_listMacros.InsertString (count, temp.name);
		_listMacros.SetCurSel (count);

		g_macros.push_back (temp);
		_macro_changed = true;
	}

	SetTextRecCount();
}

void Ckey_macroDlg::OnBnClickedButtonCopyMacro()
{
	int sel = _listMacros.GetCurSel ();
	if (sel < 0) return;

	int count = _listMacros.GetCount ();
	sMacro &macro = g_macros[sel];

	_listMacros.InsertString (count, macro.name);
	_listMacros.SetCurSel (count);

	g_macros.push_back (macro);
	_macro_changed = true;

	SetTextRecCount();
}

void Ckey_macroDlg::OnBnClickedButtonDeleteMacro()
{
	int sel = _listMacros.GetCurSel ();
	if (sel < 0) return;

	_listMacros.DeleteString (sel);
	_listMacros.SetCurSel (sel);

	g_macros.erase (g_macros.begin() + sel);
	_macro_changed = true;

	SetTextRecCount();
}

void Ckey_macroDlg::OnLbnDblclkListMacros()
{
	OnBnClickedButtonEditMacro();
}

void Ckey_macroDlg::OnBnClickedButtonUp()
{
	int sel = _listMacros.GetCurSel ();
	if (sel < 0) return;

	if (1 <= sel) {
	   _listMacros.DeleteString (sel);
	   _listMacros.InsertString (sel-1, g_macros[sel].name);
	   _listMacros.SetCurSel (sel-1);

	   std::swap (g_macros[sel], g_macros[sel-1]);
		_macro_changed = true;
	}
}

void Ckey_macroDlg::OnBnClickedButtonDown()
{
	int sel = _listMacros.GetCurSel ();
	if (sel < 0) return;

	if (sel < _listMacros.GetCount ()-1) { 
	   _listMacros.DeleteString (sel);
	   _listMacros.InsertString (sel+1, g_macros[sel].name);
	   _listMacros.SetCurSel (sel+1);

		std::swap (g_macros[sel], g_macros[sel+1]);
		_macro_changed = true;
	}
}

void Ckey_macroDlg::OnBnClickedButtonSave()
{
	// ��ũ�θ� ������ ���� �̸��� ��������, ��ũ�θ� �� ���� �̸����� �����Ѵ�.
	GetDlgItemText (IDC_EDIT_MACRO_FILE, g_ini.macroFileName, MAX_PATH);
	g_ini.macroFileName[MAX_PATH] = '\0';
	
	SaveMacro (g_ini.macroFileName);
	_macro_changed = false;
}


void Ckey_macroDlg::OnBnClickedButtonQuit()
{
	// �������� INI���Ͽ� �����ϱ� ���� ���̾�α׿� ������ ���� �����´�.
	g_ini.eventDelay = GetDlgItemInt (IDC_EDIT_EVENT_MIN_DELAY, NULL, FALSE);
	g_ini.eventDelay = BOUND (g_ini.eventDelay, 1, 100000);

	// ��ũ�ΰ� ����Ǿ����� ���� ���θ� ����� �����Ѵ�.
	if (_macro_changed) {
		int ret = AfxMessageBox ("��ũ�ΰ� ����Ǿ����ϴ�. �����ұ��?", MB_YESNO|MB_ICONQUESTION);
		if (ret == IDYES) {
			OnBnClickedButtonSave ();
		}
	}

	// ���⼭ ����
	OnOK ();
}

void Ckey_macroDlg::OnBnClickedCheckImeHanEng()
{
	g_ini.macroOptions.CHECK_IME_HAN_ENG = (IsDlgButtonChecked (IDC_CHECK_IME_HAN_ENG) == BST_CHECKED) ? 1 : 0;
}

void Ckey_macroDlg::OnBnClickedCheckReleaseAllKey()
{
	g_ini.macroOptions.RELEASE_ALL_KEYS = (IsDlgButtonChecked (IDC_CHECK_RELEASE_ALL_KEY) == BST_CHECKED) ? 1 : 0;
}
