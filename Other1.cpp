#include <tlist.h>
#include <tnode.h>
#include <cstring>
#include <iostream>
#include <iomanip>

template <typename T>
TList<T>::TList()
{
first = NULL;
last = NULL; 
size = 0;
}

template <typename T>
TList<T>::TList(T val, int num)
{
first = NULL; 
last = NULL;
size = 0;
for (i = 0; i < num; i++)
  {
   InsertFront(val);
  }
}

template <typename T>
bool TList<T>::IsEmpty() const
{
if (first == NULL)
{
return true;
}
else
return false;
}

template <typename T>
void TList<T>::Clear()
{
while (!IsEmpty())
{
RemoveFront();
}
}

template <typename T>
TList<T>::~TList()
{
Clear();
}

template <typename T>
TList<T>::TList(const TList& L)
{
first = NULL;
last = NULL;
size = 0;
TListIterator<T> i = L.GetIterator();
while (i.HasCurrent())
{
InsertBack(i.GetData());
i.Next();
} 
}

template <typename T>
TList<T>& TList<T>::operator=(const  TList<T>& L)
{
Clear();
TListIterator<T> i = L.GetIterator();
while (i.HasCurrent())
{
InsertBack(i.GetData());
i.Next();
}
}

template <typename T>
TList<T>& TList<T>::TList<T>(TList && L)
{
first = L.first;
last = L.last;
size = L.size;
L.first = NULL; 
L.last = NULL; 
L.size = 0;
}

template <typename T>
TList<T>& TList<T>::operator=(TList && L);
{
Clear();
first = L.first;
last = L.last;
size = L.size;
L.first = NULL;
L.last = NULL;
L.size = 0;
}

template <typename T>
int TList<T>::GetSize() const
{
size = 0;
if (ptr != NULL)
{
size++;
ptr = ptr->next
}
return size;
}

template <typename T>
void TList<T>::InsertFront(const T& d);
{
TNode<T>* node = new TNode<T>(d);
first->prev = node;
node->next = first;
first = node;
}

template <typename T>
void TList<T>::InsertBack(const T& d);
{
TNode<T>* node = new TNode<T>(d);
last->next = node;
node->prev = last;
last = node;
}

template <typename T>
void TList<T>::RemoveFront();
{
if (IsEmpty())
 return;
if (GetSize() == 1) 
{
 delete first;
 first = NULL;
 last = NULL;
}
else 
{
TNode<T>* node = first;
first = first->next;
first->prev = NULL;
delete node;
}
size--;
}

template <typename T>
void TList<T>::RemoveBack()
{
if (IsEmpty())
 returnl
if (GetSize() == 1)
{
 delete last;
 first = NULL;
 last = NULL;
}
else
{
Tnode<T>* node = last;
last = last->prev;
last->next = NULL;
delete node;
}
size--;
}

template <typename T>
T& TList<T>::GetFirst() const
{
return first->data;
}

template <typename T>
T& TList<T>::GetLast() const
{
return last->data;
}

template <typename T>
TListIterator<T> TList<T>::GetIterator() const
{
TListIterator<T> i;
i.ptr = first;
return i;
}

template <typename T>
TListIterator<T> TList<T>::GetIteratorEnd() const
{
TListIterator<T> i;
i.ptr = last;
return i;
}

template <typename T>
void TList<T>::Insert(TListIterator<T> pos, const T& d)
{
if (GetSize() == 0)
{
// insert single item 
// doesn't reger to node, insert at end of list 
}
TNode<T>* node = new TNode<T>(d);
node->prev = pos.ptr->prev;
node->next = pos.ptr;
node->prev->next = node;
node->next->prev = node;
size++;
}

template <typename T>
TListIterator<T> TList<T>::Remove(TListIterator<T> pos)
{




}

void TList<T>::Print(std::ostream& os, char delim = ' ') const
{
while (ptr != NULL || ptr->next != NULL)
{
node = pos.ptr;
cout node;
}

template <typename T>
TList<T> operator+(const TList<T>& t1, const TList<T>& t2)
{
TList<T> newT = t1;
for (TListIterator<T> i = newT.GetIterator(); i.HasNext(); i = i.Next())
  {
   newT.InsertBack(i.GetData());
  }
newT.InsertBack(t2.GetLast());
}


TListIterator<T>::TListIterator()
{
ptr = NULL;
}

template <typename T>
bool TListIterator<T>::HasNext() const
{
if (ptr == NULL)
{
  return false; 
}
if (ptr->next == NULL)
{
 return false
}
 return true;
}

template <typename T>
bool TListIterator<T>::HasPrevious() const
{
if (ptr == NULL || ptr->prev == NULL)
{
  return false
}
  return true;
}

template <typename T>
TListIterator<T> TListIterator<T>::Next()
{
ptr = ptr->next;
return *this;
}    

template <typename T>
TListIterator<T> TListIterator<T>::Previous()
{
ptr = ptr->prev;
return *this;
}

template <typename T>
T& TListIterator<T>::GetData() const
{
if (ptr == NULL)
{
return TList<T>::dummy;
}
else 
return ptr->data;
}

template <typename T>
bool TListIterator<T>::HasCurrent()
{
if (ptr != NULL)
return true;
else
return false;
}
