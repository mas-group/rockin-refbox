
/***************************************************************************
 *  menus.cpp - LLSF RefBox shell menus
 *
 *  Created: Sun Mar 03 00:29:20 2013
 *  Copyright  2013  Tim Niemueller [www.niemueller.de]
 ****************************************************************************/

/*  Redistribution and use in source and binary forms, with or without
 *  modification, are permitted provided that the following conditions
 *  are met:
 *
 * - Redistributions of source code must retain the above copyright
 *   notice, this list of conditions and the following disclaimer.
 * - Redistributions in binary form must reproduce the above copyright
 *   notice, this list of conditions and the following disclaimer in
 *   the documentation and/or other materials provided with the
 *   distribution.
 * - Neither the name of the authors nor the names of its contributors
 *   may be used to endorse or promote products derived from this
 *   software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 * FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
 * INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
 * STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
 * OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#include "menus.h"

namespace llsfrb_shell {
#if 0 /* just to make Emacs auto-indent happy */
}
#endif


Menu::Menu(NCursesWindow *parent, int n_items, NCursesMenuItem **items)
  : NCursesMenu(n_items + 2, max_cols(n_items, items) + 2,
		(parent->lines() - max_cols(n_items, items))/2,
		(parent->cols() - max_cols(n_items, items))/2),
    parent_(parent)
{
  set_mark("");
  InitMenu(items, true, true);
}

void
Menu::On_Menu_Init()
{
  bkgd(' '|COLOR_PAIR(0));
  //subWindow().bkgd(parent_->getbkgd());
  refresh();
}

int
Menu::max_cols(int n_items, NCursesMenuItem **items)
{
  int rv = 0;
  for (int i = 0; i < n_items; ++i) {
    rv = std::max(rv, (int)strlen(items[i]->name()));
  }
  return rv;
}

MachineWithPuckMenu::MachineWithPuckMenu(NCursesWindow *parent,
					 std::shared_ptr<llsf_msgs::MachineInfo> minfo)
  : NCursesMenu(det_lines(minfo) + 1 + 2, 8 + 2,
		(parent->lines() - (det_lines(minfo) + 1))/2,
		(parent->cols() - 8)/2)
{
  int n_items = det_lines(minfo);
  items_.resize(n_items + 1);
  int ni = 0;
  NCursesMenuItem **mitems = new NCursesMenuItem*[2 + n_items];
  for (int i = 0; i < minfo->machines_size(); ++i) {
    const llsf_msgs::Machine &m = minfo->machines(i);
    if (m.has_puck_under_rfid()) {
      items_[ni++] = std::make_tuple(m.name() + "  " +
				     llsf_msgs::PuckState_Name(m.puck_under_rfid().state()),
				     m.name(), m.puck_under_rfid().id());
    }
    for (int l = 0; l < m.loaded_with_size(); ++l) {
      items_[ni++] = std::make_tuple(m.name() + "  " +
				     llsf_msgs::PuckState_Name(m.loaded_with(l).state()),
				     m.name(), m.loaded_with(l).id());
    }
  }
  for (int i = 0; i < ni; ++i) {
    SignalItem *item = new SignalItem(std::get<0>(items_[i]));
    item->signal().connect(boost::bind(&MachineWithPuckMenu::puck_selected, this,
				       std::get<1>(items_[i]), std::get<2>(items_[i])));
    mitems[i] = item;
  }
  s_cancel_ = "Cancel";
  mitems[ni] = new SignalItem(s_cancel_);
  mitems[ni+1] = new NCursesMenuItem();

  set_mark("");
  InitMenu(mitems, true, true);
  frame("Puck");
}

void
MachineWithPuckMenu::puck_selected(std::string machine, unsigned int puck_id)
{
  sig_puck_sel_(machine, puck_id);
}

void
MachineWithPuckMenu::On_Menu_Init()
{
  bkgd(' '|COLOR_PAIR(0));
  //subWindow().bkgd(parent_->getbkgd());
  refresh();
}

int
MachineWithPuckMenu::det_lines(std::shared_ptr<llsf_msgs::MachineInfo> &minfo)
{
  int rv = 0;
  for (int i = 0; i < minfo->machines_size(); ++i) {
    const llsf_msgs::Machine &m = minfo->machines(i);
    if (m.has_puck_under_rfid()) {
      rv += 1;
    }
    rv += m.loaded_with_size();
  }
  return rv;
}


MachineThatCanTakePuckMenu::MachineThatCanTakePuckMenu(
  NCursesWindow *parent,
  std::shared_ptr<llsf_msgs::MachineInfo> minfo)
  : NCursesMenu(det_lines(minfo) + 1 + 2, 8 + 2,
		(parent->lines() - (det_lines(minfo) + 1))/2,
		(parent->cols() - 8)/2),
    minfo_(minfo)
{
  machine_selected_ = false;
  int n_items = det_lines(minfo);
  items_.resize(n_items);
  int ni = 0;
  NCursesMenuItem **mitems = new NCursesMenuItem*[2 + n_items];
  for (int i = 0; i < minfo->machines_size(); ++i) {
    const llsf_msgs::Machine &m = minfo->machines(i);
    if (! m.has_puck_under_rfid() || (m.inputs_size() - m.loaded_with_size() > 0)) {
      items_[ni++] = std::make_tuple(m.name(), i);
    }
  }
  std::sort(items_.begin(), items_.end());

  for (int i = 0; i < ni; ++i) {
    SignalItem *item = new SignalItem(std::get<0>(items_[i]));
    item->signal().connect(boost::bind(&MachineThatCanTakePuckMenu::machine_selected, this,
				       std::get<1>(items_[i])));
    mitems[i] = item;
  }
  s_cancel_ = "Cancel";
  mitems[ni] = new SignalItem(s_cancel_);
  mitems[ni+1] = new NCursesMenuItem();

  set_mark("");
  set_format(ni+1, 1);
  InitMenu(mitems, true, true);
  frame("Machine");
}

void
MachineThatCanTakePuckMenu::machine_selected(int i)
{
  machine_selected_ = true;
  machine_idx_ = i;
}

const llsf_msgs::Machine &
MachineThatCanTakePuckMenu::machine()
{
  return minfo_->machines(machine_idx_);
}

void
MachineThatCanTakePuckMenu::On_Menu_Init()
{
  bkgd(' '|COLOR_PAIR(0));
  //subWindow().bkgd(parent_->getbkgd());
  refresh();
}

int
MachineThatCanTakePuckMenu::det_lines(std::shared_ptr<llsf_msgs::MachineInfo> &minfo)
{
  int rv = 0;
  for (int i = 0; i < minfo->machines_size(); ++i) {
    const llsf_msgs::Machine &m = minfo->machines(i);
    if (! m.has_puck_under_rfid() || (m.inputs_size() - m.loaded_with_size() > 0)) {
      rv += 1;
    }
  }
  return rv;
}

MachineThatCanTakePuckMenu::operator bool() const
{
  return machine_selected_;
}


PuckForMachineMenu::PuckForMachineMenu(NCursesWindow *parent,
				       std::shared_ptr<llsf_msgs::PuckInfo> pinfo,
				       std::shared_ptr<llsf_msgs::MachineInfo> minfo,
				       const llsf_msgs::Machine &machine)
  : NCursesMenu(det_lines(pinfo, minfo, machine) + 1 + 2, 14 + 2,
		(parent->lines() - (det_lines(pinfo, minfo, machine) + 1))/2,
		(parent->cols() - 14)/2),
    pinfo_(pinfo)
{
  puck_selected_ = false;
  std::list<int> rel_pucks = relevant_pucks(pinfo, minfo, machine);
  items_.resize(rel_pucks.size() + 1);
  int ni = 0;
  NCursesMenuItem **mitems = new NCursesMenuItem*[2 + rel_pucks.size()];
  std::list<int>::iterator i;
  for (i = rel_pucks.begin(); i != rel_pucks.end(); ++i) {
    const llsf_msgs::Puck &p = pinfo->pucks(*i);
    items_[ni++] = std::make_tuple(llsf_msgs::PuckState_Name(p.state()) + " (" +
				   std::to_string(p.id()) + ")", *i);
  }
  //std::sort(items_.begin(), items_.end());

  for (int i = 0; i < ni; ++i) {
    SignalItem *item = new SignalItem(std::get<0>(items_[i]));
    item->signal().connect(boost::bind(&PuckForMachineMenu::puck_selected, this,
				       std::get<1>(items_[i])));
    mitems[i] = item;
  }
  s_cancel_ = "Cancel";
  mitems[ni] = new SignalItem(s_cancel_);
  mitems[ni+1] = new NCursesMenuItem();

  set_format(ni+1, 1);
  set_mark("");
  InitMenu(mitems, true, true);
  frame("Puck");
}

void
PuckForMachineMenu::puck_selected(int i)
{
  puck_selected_ = true;
  puck_idx_ = i;
}

const llsf_msgs::Puck &
PuckForMachineMenu::puck()
{
  return pinfo_->pucks(puck_idx_);
}

void
PuckForMachineMenu::On_Menu_Init()
{
  bkgd(' '|COLOR_PAIR(0));
  //subWindow().bkgd(parent_->getbkgd());
  refresh();
}

std::list<int>
PuckForMachineMenu::relevant_pucks(std::shared_ptr<llsf_msgs::PuckInfo> &pinfo,
				   std::shared_ptr<llsf_msgs::MachineInfo> &minfo,
				   const llsf_msgs::Machine &machine)
{
  std::list<int> rv;
  for (int i = 0; i < pinfo->pucks_size(); ++i) {
    rv.push_back(i);
  }

  // filter out all pucks which are already bound at a machine
  rv.remove_if([&minfo,&pinfo](int p)
	       {
		 for (int i = 0; i < minfo->machines_size(); ++i) {
		   const llsf_msgs::Machine &m = minfo->machines(i);
		   if (m.has_puck_under_rfid() && m.puck_under_rfid().id() == pinfo->pucks(p).id()) {
		     return true;
		   }
		   for (int j = 0; j < m.loaded_with_size(); ++j) {
		     if (m.loaded_with(j).id() == pinfo->pucks(p).id()) {
		       return true;
		     }
		   }
		 }
		 return false;
	       });

  if (machine.inputs_size() > 0) {
    // filter out all pucks which are not avalid input for the current machine
    rv.remove_if([&pinfo,&machine](int p)
		 {
		   for (int i = 0; i < machine.inputs_size(); ++i) {
		     if (pinfo->pucks(p).state() == machine.inputs(i)) return false;
		   }
		   return true;
		 });
  }

  // filter out all pucks in a state already placed at the machine
  rv.remove_if([&pinfo,&machine](int p)
	       {
		 if (machine.has_puck_under_rfid() &&
		     machine.puck_under_rfid().state() == pinfo->pucks(p).state())
		 {
		   return true;
		 }
	
		 for (int i = 0; i < machine.loaded_with_size(); ++i) {
		   if (pinfo->pucks(p).state() == machine.loaded_with(i).state()) return true;
		 }
		 return false;
	       });

  return rv;    
}

int
PuckForMachineMenu::det_lines(std::shared_ptr<llsf_msgs::PuckInfo> &pinfo,
			      std::shared_ptr<llsf_msgs::MachineInfo> &minfo,
			      const llsf_msgs::Machine &machine)
{
  return relevant_pucks(pinfo, minfo, machine).size();
}

PuckForMachineMenu::operator bool() const
{
  return puck_selected_;
}


MachinePlacingMenu::MachinePlacingMenu(NCursesWindow *parent,
				       std::string machine, std::string puck)
  : NCursesMenu(5, 30, (parent->lines() - 5)/2, (parent->cols() - 30)/2)
{
  valid_selected_ = false;
  place_under_rfid_ = false;
  s_under_rfid_ = "Place " + puck.substr(0,2) + " under RFID of " + machine;
  s_loaded_with_ = "Load " + machine + " with " + puck.substr(0,2);
  s_cancel_ = "Cancel";
  NCursesMenuItem **mitems = new NCursesMenuItem*[4];

  SignalItem *item_0 = new SignalItem(s_under_rfid_);
  SignalItem *item_1 = new SignalItem(s_loaded_with_);
  mitems[0] = item_0;
  mitems[1] = item_1;
  mitems[2] = new SignalItem(s_cancel_);
  mitems[3] = new NCursesMenuItem();
    
  item_0->signal().connect(boost::bind(&MachinePlacingMenu::item_selected, this, true));
  item_1->signal().connect(boost::bind(&MachinePlacingMenu::item_selected, this, false));

  set_mark("");
  set_format(3, 1);
  InitMenu(mitems, true, true);
  frame("Placing");
}

void
MachinePlacingMenu::item_selected(bool under_rfid)
{
  valid_selected_ = true;
  place_under_rfid_ = under_rfid;
}

bool
MachinePlacingMenu::place_under_rfid()
{
  return place_under_rfid_;
}

void
MachinePlacingMenu::On_Menu_Init()
{
  bkgd(' '|COLOR_PAIR(0));
  //subWindow().bkgd(parent_->getbkgd());
  refresh();
}

MachinePlacingMenu::operator bool() const
{
  return valid_selected_;
}


} // end of namespace llsfrb
