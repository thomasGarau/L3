package exo3;

public class EventHandler {

	private Object entity;
	private EventInterceptor ei;
	
	public EventHandler(Object entity, EventInterceptor ei) {
		this.entity = entity;
		this.ei = ei;
	}
	
	public void handleEvent(Event event){
		event.traiter(ei, entity);
	}
		

}
