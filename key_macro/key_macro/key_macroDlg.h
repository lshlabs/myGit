#pragma once
#include "afxwin.h"
#include "HyperLink.h"
#include "DialogCommon.h"


class Ckey_macroDlg : public CDialogCommon
{
public:
	Ckey_macroDlg(CWnd* pParent = NULL);	// ǥ�� �������Դϴ�.
	~Ckey_macroDlg();

	enum { IDD = IDD_KEY_MACRO_DIALOG };

	void OnKeybdMouseEvent (BYTE vk_code, bool vk_pressed);

private:
	DWORD _macro_exec_time;
	
	void SetTextRecCount();
	void EnableDlgItem(BOOL enable);

protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV �����Դϴ�.

	DECLARE_MESSAGE_MAP()

	HICON m_hIcon;
	// ��ũ�� ����� ǥ���ϱ� ���� ����Ʈ�ڽ��� �� ���� ����Ѵ�.
	// �ϳ��� ���� ���¿��� �����ִ� ��(���� ����)�̰�,
	// �ٸ� �ϳ��� ���� �����¿��� �����ִ� ��(��Ƽ ����)�̴�.
	CListBox _listMacros;
	CListBox _listMacros2;
	// Ȩ������ ��ũ�� ǥ��
	CHyperLink	_staticHomepage;

	virtual BOOL OnInitDialog();
	afx_msg HCURSOR OnQueryDragIcon();
	afx_msg void OnRawInput(UINT nInputcode, HRAWINPUT hRawInput);
	afx_msg void OnPaint();
	afx_msg void OnDestroy();
	afx_msg void OnTimer(UINT_PTR nIDEvent);
	afx_msg void OnCbnSelchangeComboKey();
	afx_msg void OnBnClickedRadioRun();
	afx_msg void OnBnClickedRadioEdit();
	afx_msg void OnBnClickedButtonAddMacro();
	afx_msg void OnBnClickedButtonDeleteMacro();
	afx_msg void OnBnClickedButtonCopyMacro();
	afx_msg void OnBnClickedButtonEditMacro();
	afx_msg void OnBnClickedButtonMacroFile();
	afx_msg void OnBnClickedButtonRecMacro();
	afx_msg void OnBnClickedButtonUp();
	afx_msg void OnBnClickedButtonDown();
	afx_msg void OnLbnDblclkListMacros();
	afx_msg void OnBnClickedButtonSave();
	afx_msg void OnBnClickedOk();
	afx_msg void OnBnClickedCancel();
	afx_msg void OnBnClickedButtonQuit();
	afx_msg void OnBnClickedCheckImeHanEng();
public:
	afx_msg void OnBnClickedCheckReleaseAllKey();
};
