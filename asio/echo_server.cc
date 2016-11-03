#include <iostream>
#include <cstdlib>
#include <boost/bind.hpp>
#include <boost/asio.hpp>
#include <memory>
#include <vector>
#include <unordered_map>

using namespace std;

using boost::asio::ip::tcp;

class Server;
class Session;
class SessionMgr;

class GuidMgr {
private:
  /*
  error: must be static const/
  static int no_ = 0;
  */
  static int no_;

public:
  static int NewGuid() {
    return ++no_;
  }
};

/*
echo_server.cc:25:21: error: 'static' may not be used when defining (as opposed to declaring) a static data member [-fpermissive]
static int GuidMgr::no_ = 0;   // 初始化时不能带static
*/
int GuidMgr::no_ = 0;

/*
因为SessionMgr成员函数定义中用了Session，必须在Session定义后或头文件后才能使用，
Session和SessionMgr有相互引用，两个类的内容都在类中定义编译不通过，uncompleted class，
一般做法是分开头文件和定义文件
*/
class SessionMgr {
private:
  unordered_map<int, shared_ptr<Session> > session_map_;
public:
  void AddSession(shared_ptr<Session> new_session);
  void RemoveSession(int guid);
  void Dump();
};

SessionMgr g_session_mgr;

class Session {
private:
  tcp::socket socket_;
  char data_[1024];
  int guid_;

public:
  int GetGuid() {
    return guid_;
  }
  void SetGuid(int &guid) {
    guid_ = guid;
  }

  Session(boost::asio::io_service& io_service):
    socket_(io_service), guid_(0) {
  }

  tcp::socket &socket() {
    return this->socket_;
  }

  void Start() {
    socket_.async_read_some(
        boost::asio::buffer(data_, 1024),
        boost::bind(&Session::HandleRead, this,
            boost::asio::placeholders::error,
            boost::asio::placeholders::bytes_transferred));
  }

  void HandleRead(
      const boost::system::error_code &error,
      size_t bytes_transferred) {
    if (!error) {
      cout << data_ << endl;
      cout << bytes_transferred << endl;
      boost::asio::async_write(
          socket_,
          boost::asio::buffer(data_, bytes_transferred),
          boost::bind(&Session::HandleWrite, this,
                      boost::asio::placeholders::error));
    } else {
      g_session_mgr.RemoveSession(guid_);
      g_session_mgr.Dump();
      cout << __LINE__ << " " << error << endl;
    }
  }

  void HandleWrite(const boost::system::error_code &error) {
    if (!error) {
      socket_.async_read_some(
          boost::asio::buffer(data_, 1024),
          boost::bind(
              &Session::HandleRead, this,
              boost::asio::placeholders::error,
              boost::asio::placeholders::bytes_transferred));
    } else {
      g_session_mgr.RemoveSession(guid_);
      g_session_mgr.Dump();
      cout << __LINE__ << " " << error << endl;
    }
  }

  friend ostream& operator<<(ostream &os, Session &c);
};

/* 输出运算符重载 */
ostream& operator<<(ostream &os, Session &c) {
  // os << "[session]" << c.guid_ << " " << c.socket_ << endl;
  os << "[session]" << c.guid_ << endl;
  return os;
}

class Server {
private:
  boost::asio::io_service& io_service_;
  tcp::acceptor acceptor_;
public:
  
  Server(boost::asio::io_service& io_service, short port):
      io_service_(io_service),
      acceptor_(io_service, tcp::endpoint(tcp::v4(), port)) {        
    shared_ptr<Session> new_session(new Session(io_service_));
    g_session_mgr.AddSession(new_session);
    g_session_mgr.Dump();
    acceptor_.async_accept(
        new_session->socket(),
        boost::bind(
            &Server::HandleAccept, this,
            new_session,
            boost::asio::placeholders::error));
  }

  void HandleAccept(shared_ptr<Session> new_session,
      const boost::system::error_code &error) {
    cout << __LINE__ << " " << error << endl;
    if (!error) {
      new_session->Start();

      shared_ptr<Session> new_session1(new Session(io_service_));
      g_session_mgr.AddSession(new_session1);
      g_session_mgr.Dump();
      acceptor_.async_accept(new_session1->socket(),
            boost::bind(&Server::HandleAccept, this, new_session1,
                        boost::asio::placeholders::error));
    } else {

      cout << __LINE__ << " " << error << endl;
      new_session.reset();
    }
  }
};

/*
note: 成员变量为引用时如何处理
http://blog.csdn.net/lazyq7/article/details/48186291
*/

void SessionMgr::AddSession(shared_ptr<Session> new_session) {
  int guid = GuidMgr::NewGuid();
  cout << __LINE__ << " " << guid << endl;
  new_session->SetGuid(guid);
  session_map_[guid] = new_session;
}

void SessionMgr::RemoveSession(int guid) {
  /*
  map的erase删除一个元素，如果key不存在时，返回0，返回即为删除的元素个数
  */
  int erase_num = session_map_.erase(guid);
  cout << __LINE__ << " " << guid << " " << erase_num << endl;
}

void SessionMgr::Dump() {
  cout << __LINE__ << "-------dump start----------" << endl;
  for(auto const& entry : session_map_) {
    cout << entry.first << " " << entry.second << endl;
  }
  cout << __LINE__ << "--------dump end---------" << endl;
}

int main() {
  try {
    boost::asio::io_service io_service;
    Server s(io_service, 48000);
    io_service.run();
  } catch (exception& e) {
    cout << "exception" << e.what() << endl;
  }
}


