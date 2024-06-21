#pragma once
#include "afxwin.h"
#include "macro_def.h"

class CListBoxEx : public CListBox {
public:
	CListBoxEx ();
	
	void SetMacroItems (vector<sMacroItem> *items) { _items = items; }

	int GetFirstSel ();
	int GetLastSel ();

private:
	bool ctrl;
	vector<sMacroItem> *_items;
	vector<sMacroItem> clipboard;

	void KeyDown_CtrlA ();
	void KeyDown_CtrlC ();
	void KeyDown_CtrlV ();
	void KeyDown_CtrlX ();
	void KeyDown_Delete ();

protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV support

	DECLARE_MESSAGE_MAP()
private:
	afx_msg void OnChar(UINT nChar, UINT nRepCnt, UINT nFlags);
	afx_msg void OnKeyDown(UINT nChar, UINT nRepCnt, UINT nFlags);
	afx_msg void OnKeyUp(UINT nChar, UINT nRepCnt, UINT nFlags);
};

